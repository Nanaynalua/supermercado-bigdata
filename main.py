from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados
class Venda(BaseModel):
    id: int
    produto: str
    categoria: str
    valor: float
    data: str

# Dados simulados
vendas_db = [
    Venda(id=1, produto="Arroz", categoria="Alimentos", valor=19.90, data="2025-10-01"),
    Venda(id=2, produto="Detergente", categoria="Limpeza", valor=3.50, data="2025-10-02"),
    Venda(id=3, produto="Refrigerante", categoria="Bebidas", valor=6.99, data="2025-10-03"),
]

# Endpoint raiz
@app.get("/")
def home():
    return {"mensagem": "API do supermercado funcionando!"}

# Endpoint de vendas
@app.get("/vendas", response_model=List[Venda])
def listar_vendas():
    return vendas_db
