# <p align="center">📈 FINTECH DATA PIPELINE</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge" alt="Matplotlib">
</p>

<p align="center">
  <strong>Pipeline ETL Automatizado.</strong> Script desenvolvido em Python para extração de dados cambiais em tempo real via API, transformação estruturada e armazenamento seguro em Banco de Dados Relacional SQL.
</p>

---

## 🚀 Arquitetura do Sistema (Fluxo ETL)

O projeto foi desenhado seguindo as melhores práticas de Engenharia de Dados, dividindo o processo em três camadas fundamentais:

| Etapa | Operação | Tecnologia | Descrição |
| :--- | :--- | :--- | :--- |
| **E**xtract | Consumo de API | `Requests` | Captura em tempo real das cotações de fechamento do Dólar (USD) e Euro (EUR). |
| **T**ransform | Modelagem de Dados | `Pandas` / `Datetime` | Limpeza dos dados brutos em JSON, extração de strings, conversão de tipos (float) e timestamp da consulta. |
| **L**oad | Persistência Relacional | `SQLite3` | Armazenamento incremental automático (`append`) na tabela relacional `historico_moedas`. |

---

## 📊 Visualização e Inteligência de Negócio

O sistema conta com um módulo independente de análise que se conecta via queries SQL ao banco de dados e gera inteligência visual automatizada:

*   **Query Customizada:** Execução de comandos `SELECT` estruturados para ler os registros históricos.
*   **Análise de Tendência:** Plotagem de gráfico de linhas com marcadores dinâmicos comparando a evolução do Dólar vs. Euro.
*   **Apoio à Decisão:** Interface limpa com grades estatísticas, legendas automáticas e dimensionamento responsivo (`tight_layout`).




