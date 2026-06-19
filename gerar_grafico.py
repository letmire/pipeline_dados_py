import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

conexao = sqlite3.connect("c:/Users/letmi/cotacoes_banco.db")
comando_sql = "SELECT data_consulta, valor_dolar, valor_euro FROM historico_moedas"
df = pd.read_sql(comando_sql, conexao)

conexao.close()

plt.figure(figsize=(10, 5))  

plt.plot(df["data_consulta"], df["valor_dolar"], label="Dólar (USD)", color="green", marker="o")
plt.plot(df["data_consulta"], df["valor_euro"], label="Euro (EUR)", color="blue", marker="o")

plt.title("Histórico de Cotações - Pipeline de Dados", fontsize=14, fontweight='bold')
plt.xlabel("Data e Hora da Consulta", fontsize=12)
plt.ylabel("Valor em Reais (R$)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)  
plt.legend()  

plt.tight_layout()

# Mostra o gráfico na tela!
print("Abrindo o gráfico visual...")
plt.show()