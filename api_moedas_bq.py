import base64
import pandas as pd
from datetime import datetime, timedelta
from bcb import currency
from google.cloud import bigquery

def get_cotacao_moeda(moedas, data_inicio, data_fim):
    dados = currency.get(moedas, start=data_inicio, end=data_fim)
    return dados.reset_index()

def import_bq(d_frame, table_name):
    client = bigquery.Client()
    dataset_id = "api_moedas"
    table_ref = client.dataset(dataset_id).table(table_name)
    
    # Carrega dados
    job = client.load_table_from_dataframe(d_frame, table_ref)
    job.result()
    print(f"Dados importados: {table_ref.table_id}")

def main(event, context=None):
    data_inicial = datetime.today() - timedelta(days=1)
    data_final = datetime.today()
    dados = get_cotacao_moeda(
        ['ARS', 'COP', 'USD', 'CLP'],
        data_inicial.strftime('%Y-%m-%d'),
        data_final.strftime('%Y-%m-%d')
    )    
    import_bq(dados, "historico_cotacoes")
    print("Processamento concluído!")
    return "Processamento concluído com sucesso!"