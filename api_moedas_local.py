# Pacotes Utilizados
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
from bcb import currency
from pandas_gbq import to_gbq
import os
from dotenv import load_dotenv

# Carrega objeto do tipo '.env' com as credenciais de escrita no Big Query
load_dotenv()

#Usamos a função currancy para pegar a cotação das moeda, em Real, no período
def get_cotacao_moeda(moedas, data_inicio, data_fim):
    dados = currency.get(moedas, start=data_inicio, end=data_fim)
    dados = dados.reset_index()
    dados = pd.DataFrame(dados)
    return dados



# Função de escrita no Big Query
def load_to_bq(data_frame, dataset_id, table_id, project_id):
    try:
        # Define a referência da tabela
        table_ref = f"{dataset_id}.{table_id}"
        
        # Escreve o DataFrame no BigQuery
        to_gbq(
            data_frame,
            destination_table=table_ref,
            project_id=project_id,
            if_exists='append',  # Pode ser 'replace', 'append' ou 'fail'
        )
        print("Carga para o BigQuery concluída com sucesso.")

    except Exception as e:
        print(f"Erro ao carregar dados para o BigQuery: {e}")


#Função principal
def main():
    data_inicial =datetime.today() - timedelta(days=365)
    data_final = datetime.today()
    data_inicial = data_inicial.strftime('%Y-%m-%d')
    data_final = data_final.strftime('%Y-%m-%d')
    moedas = ['ARS', 'COU', 'USD', 'CLP'] # Moedas a serem cotadas
    dados = get_cotacao_moeda(moedas, data_inicial, data_final)

    data_frame  = dados
    dataset_id = 'api_moedas'  # Dataset do BigQuery
    table_id = 'historico_cotacoes'      # Tabela no BigQuery - Cria ou faz o append
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')  # ID do projeto no BigQuery (presente no .env com o JSON com as credenciais de Acesso).
    load_to_bq(data_frame, dataset_id, table_id, project_id)

if __name__ == "__main__":
    main()
