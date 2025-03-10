# ETL API de Cotações
Repositório de teste para integração de dados ao Big Query utilizando o Cloud Functions para um ETL utilizando dados de cotação do Banco Central do Brasil.

O acionador utilizado foi o Pub/Sub.

## Como utilizar um ambiente virtual no Python
Um ambiente virtual é um ambiente isolado que permite gerenciar dependências de um projeto Python separadamente do sistema global. Ele evita conflitos entre versões de pacotes e facilita a replicação do ambiente em diferentes máquinas.

  1. **Criando o ambiente**: basta digitar no terminal do python o comando `python -m venv venv`
  2. **Ativando o ambiente**: Caso você seja usuário Windowns basta digitar `venv\Scripts\activate` no terminal. Caso utilize Linux ou MacOS `source venv/bin/activate`.
  3. **Instalar dependência**: Para instalar todas as dependência necessárias para executar o código, digite `pip install -r requirements.txt` no terminal do Python.
  4. **Execução do script**: para executar o script digite `python nome_do_script.py`
  5. **Atualizar dependências**: Caso seja necessário a instalação de outras bibliotecas, é possível atualizar o arquivo de "requirements.txt" com o comando `pip freeze > requirements.txt` no terminal.
