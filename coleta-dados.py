'''
_________________________________________________________________________________________________________________________________
|                                                                                                                               |
|********************************************************** DESCRIÇÃO **********************************************************|
|_______________________________________________________________________________________________________________________________|
| Neste arquivo se encontram todas as funções responsáveis pela acoleta de dados no site informado e carregamento no Google Big |
| Query                                                                                                                         |
|                                                                                                                               |
|                                                         Autor: Yago José Araújo dos Santos. Contato: yago.j.a.santos@gmail.com|
|_______________________________________________________________________________________________________________________________|
'''

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pandas as pd
from google.cloud import bigquery

# Função para carregar mais dados do site desejado
def carregaDados(driver):
    try:
        # Encontrar o botão que exibe todos os dados na mesma página e clicar nele
        next_button = driver.find_element(By.CSS_SELECTOR, '#dt-length-0 > option:nth-child(8)')
        next_button.click()
        return True
    except Exception as e:
        print(f"Erro ao carregar mais dados: {e}")
        return False

# Função que salva os dados coletados em um arquivo .csv e .xlsx localmente
def salvaLocalmente(df):
    # Salvar o DataFrame em um arquivo CSV
    df.to_csv('steamdb_sales.csv', index=False)
    print("Dados salvos em 'steamdb_sales.csv'")
    # Salvar em Excel
    df.to_excel('steamdb_sales.xlsx', index=False)
    print("Dados salvos em 'steamdb_sales.xlsx'")

# Função para realizar a coleta de dados e salvar em um pandas dataframe
def coletaDeDados():
    print('_' *50 +'\n')
    print('Coletando dados...\nPor favor, aguarde!')
    print('_' *50 +'\n')
    # Configurar o WebDriver para o Microsoft Edge
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    # URL da página de promoções do SteamDB
    url = "https://steamdb.info/sales/"
    # Abrir a página usando o Selenium
    driver.get(url)
    carregaDados(driver)
    # Esperar até que a tabela esteja presente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-sales"))
    )
    # Encontrar a tabela de promoções
    table = driver.find_element(By.CLASS_NAME, "table-sales")
    # Extrair os cabeçalhos da tabela
    headers = [header.text.strip() for header in table.find_elements(By.TAG_NAME, 'th')]
    # Extrair as linhas da tabela
    rows = []
    for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:  # Pular o cabeçalho
        cells = row.find_elements(By.TAG_NAME, 'td')
        rows.append([cell.text.strip() for cell in cells])
    # Criar um DataFrame do pandas com os dados
    df = pd.DataFrame(rows, columns=headers)
    salvaLocalmente(df)
    # Fechar o navegador
    driver.quit()

# Função para salvar dados no Google BigQuery
def salvaBigQuery(df):
    # Configurar o cliente do BigQuery
    client = bigquery.Client()
    # Definir o ID do dataset e da tabela
    dataset_id = 'caseTecnico'  # Substitua pelo seu dataset ID
    table_id = 'caseTecnicoBeAnalytic'  # Substitua pelo seu table ID
    # Referência à tabela no BigQuery
    table_ref = client.dataset(dataset_id).table(table_id)
    # Carregar o DataFrame no BigQuery
    job = client.load_table_from_dataframe(df, table_ref)
    # Esperar até que o job esteja completo
    job.result()
    # Verificar se os dados foram carregados corretamente
    table = client.get_table(table_ref)
    print(f"Carregadas {table.num_rows} linhas para a tabela {table_id}.")
    print("Dados salvos no Google BigQuery.")

# Carrega o dataframe de um arquivo .csv salvo localmente
def carregaDataframe():
    df = pd.read_csv('./steamdb_sales.csv')
    return df

# Função principal
def main():
    coletaDeDados()
    df = carregaDataframe()
    #print('VERIFICANDO DATAFRAME!')
    #print(df.head())
    #print(df.info())
    print('\n\nIniciando BigQuery...\n\n')
    salvaBigQuery(df)

main()