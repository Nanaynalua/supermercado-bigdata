from faker import Faker
import random
import requests

fake = Faker('pt_BR')

tipos_produto = ["Alimento", "Bebida", "Higiene", "Limpeza", "Pet", "Padaria", "Congelado", "Frios"]

vendas = []
for _ in range(200):
    venda = {
        "data": fake.date_between(start_date='-60d', end_date='today').isoformat(),
        "valor": round(random.uniform(5, 500), 2),
        "tipo": random.choice(tipos_produto)
    }

    if random.random() < 0.1:
        campo_faltando = random.choice(["data", "valor", "tipo"])
        venda[campo_faltando] = None

    vendas.append(venda)

url = "http://localhost:8000/vendas"
sucesso = 0
falha = 0

for venda in vendas:
    try:
        response = requests.post(url, json=venda)
        if response.status_code in [200, 201]:
            sucesso += 1
        else:
            falha += 1
    except Exception as e:
        print("Erro:", e)
        falha += 1

print(f"✅ Enviadas com sucesso: {sucesso}")
print(f"❌ Falharam: {falha}")
