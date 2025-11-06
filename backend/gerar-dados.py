from faker import Faker
import random
import pandas as pd

fake = Faker('pt_BR')

tipos = ["Alimento", "Bebida", "Higiene", "Limpeza", "Pet", "Padaria", "Congelado", "Frios"]
produtos = ["Arroz", "Feijão", "Sabonete", "Detergente", "Ração", "Pão", "Pizza", "Presunto"]
lojas = ["Loja A", "Loja B", "Loja C"]
pagamentos = ["Cartão", "Pix", "Dinheiro"]
bandeiras = ["Visa", "MasterCard", "Elo", "Hipercard"]
canais = ["Presencial", "App", "Site"]

# Gerar 700 registros únicos
vendas_unicas = []
for _ in range(700):
    forma = random.choice(pagamentos)
    venda = {
        "data": fake.date_between(start_date='-60d', end_date='today').isoformat(),
        "valor": round(random.uniform(5, 500), 2),
        "tipo": random.choice(tipos),
        "produto": random.choice(produtos),
        "loja": random.choice(lojas),
        "forma_pagamento": forma,
        "cpf_na_nota": random.choice(["Sim", "Não"]),
        "bandeira_cartao": random.choice(bandeiras) if forma == "Cartão" else "",
        "canal_venda": random.choice(canais)
    }
    vendas_unicas.append(venda)

# Criar 300 duplicatas
vendas_duplicadas = random.choices(vendas_unicas, k=300)

# Combinar e embaralhar
vendas = vendas_unicas + vendas_duplicadas
random.shuffle(vendas)

# Salvar em CSV
df = pd.DataFrame(vendas)
df.to_csv("vendas.csv", index=False)

print("✅ Arquivo vendas.csv gerado com sucesso!")
