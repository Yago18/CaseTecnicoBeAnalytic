# CaseTecnicoBeAnalytic
Desafio de seleção da empresa BeAnalytic
---

Este script realiza a coleta de dados do website [steamdb](https://steamdb.info/sales/) e os armazena no Google BigQuery.

Para execução deste script, será necessário instalar as seguintes bibliotecas:

```
pip install selenium pandas webdriver-manager google-cloud-bigquery google-auth

pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-bigquery pandas
```

O funcionamento do script segue a seguinte ordem:

* Coleta dos dados do website informado;
* Armazenamento dos dados em planilhas .csv e .xlsx;
* Autenticação e carregamento dos dados no Google BigQuery.
  * Configurar a Autenticação no Google Cloud (Este procedimento deve ser feito manualmente antes da execução do script):
    * Crie um Projeto no Google Cloud: Se você ainda não tiver um projeto no Google Cloud, crie um novo projeto.
    * Ative a API do BigQuery: No seu projeto, ative a API do BigQuery.
    * Crie uma Conta de Serviço: No Google Cloud Console, crie uma conta de serviço e baixe o arquivo JSON de credenciais.
    * Defina a Variável de Ambiente: Defina a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS para o caminho do arquivo JSON de credenciais. Exemplo: ```export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"```


[IMPORTANTE]: Para o carregamento dos dados no Google BigQuery, é necessário um arquivo .json contendo as credenciais de uma conta de seerviço para validação. Por motivos de segurança, esse arquivo não está disponível neste repositório.
