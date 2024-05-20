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

*  Coleta dos dados do website informado;
*  Armazenamento dos dados em planilhas .csv e .xlsx;
*  Autenticação e carregamento dos dados no Google BigQuery.

[IMPORTANTE]: Para o carregamento dos dados no Google BigQuery, é necessário um arquivo .json contendo as credenciais de uma conta de seerviço para validação. Por motivos de segurança, esse arquivo não está disponível neste repositório.
