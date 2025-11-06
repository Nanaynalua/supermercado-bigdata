from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "API do Supermercado Big Data"}

@app.get("/vendas")
def vendas():
    return [{"data": "2025-11-01", "valor": 1200}, {"data": "2025-11-02", "valor": 1350}]

@app.get("/produtos")
def produtos():
    return [{"nome": "Arroz", "categoria": "Grãos"}, {"nome": "Leite", "categoria": "Laticínios"}]

@app.get("/clientes")
def clientes():
    return [{"nome": "João", "fidelidade": "Alta"}, {"nome": "Maria", "fidelidade": "Média"}]

@app.get("/veracidade")
def veracidade():
    return {"limpos": 980, "sujos": 20, "errosCorrigidos": 15}

@app.get("/insights")
def insights():
    return {"produtoMaisVendido": "Leite", "horarioPico": "18h"}

@app.get("/categorias")
def categorias():
    return ["Grãos", "Laticínios", "Hortifruti", "Bebidas"]

@app.get("/grafico-vendas")
def grafico_vendas():
    return [{"hora": "08h", "qtd": 50}, {"hora": "12h", "qtd": 120}, {"hora": "18h", "qtd": 200}]
