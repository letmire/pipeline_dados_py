import sqlite3
from datetime import datetime
import pandas as pd
import requests


url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

print("Buscando cotações na internet...")
resposta = requests.get(url)
dados_brutos = resposta.json()


dolar_info = dados_brutos["USDBRL"]
euro_info = dados_brutos["EURBRL"]

dados_limpos = {
    "data_consulta": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "moeda_dolar": [dolar_info["name"].split("/")[0]],
    "valor_dolar": [float(dolar_info["bid"])],
    "moeda_euro": [euro_info["name"].split("/")[0]],
    "valor_euro": [float(euro_info["bid"])],
}

df = pd.DataFrame(dados_limpos)
print("\nDados organizados com sucesso:")
print(df)


conexao = sqlite3.connect("c:/Users/letmi/OneDrive/Desktop/Projetos/cotacoes_banco.db")
conexao = sqlite3.connect("cotacoes_banco.db")


df.to_sql("historico_moedas", conexao, if_exists="append", index=False)

# Fecha a conexão para salvar com segurança
conexao.close()
print("Dados salvos no banco SQL com sucesso!")