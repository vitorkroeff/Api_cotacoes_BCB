# pacotes utilizados
import pandas as pd
from datetime import datetime, timedelta
from bcb import currency
from google.cloud import bigquery

# função que retorna a cotação de um vetor de moedas.
# Cotações fornecidas pelo Banco Central do Brasil
def get_cotacao_moeda(moedas, data_inicio, data_fim):
    dados = currency.get(moedas, start=data_inicio, end=data_fim)
    return dados.reset_index()


# Função de Escrita no Big Query
def import_bq(d_frame, table_name):
    client = bigquery.Client()
    dataset_id = "api_moedas"
    table_ref = client.dataset(dataset_id).table(table_name)
    
    # Carrega dados
    job = client.load_table_from_dataframe(d_frame, table_ref)
    job.result()
    print(f"Dados importados: {table_ref.table_id}")


# Código a ser executado
# os parâmetros de event e context são necessários para gatilhos do tipo Pub/Sub
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
    return "Processamento concluído com sucesso!" # É necessário um retorno do tipo string, etc, pois ele é utilizado como um endpoint no Flask
