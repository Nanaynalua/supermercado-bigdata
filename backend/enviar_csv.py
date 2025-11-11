import pandas as pd
import requests

df = pd.read_csv("SampleSuperstore.csv")

# Substitui NaN por string vazia
df = df.fillna("")

# Converte para lista de dicionários
vendas = df.to_dict(orient="records")

# Envia para a API
url = "http://localhost:8000/vendas/lote"
response = requests.post(url, json=vendas)

print("✅ Resposta da API:", response.json())
