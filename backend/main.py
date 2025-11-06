from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

vendas_salvas = []  # Simulação de banco em memória

class Venda(BaseModel):
    data: str
    valor: float
    tipo: str
    produto: str
    loja: str
    forma_pagamento: str
    cpf_na_nota: str
    bandeira_cartao: str
    canal_venda: str

@app.post("/vendas/lote")
def receber_vendas(vendas: List[Venda]):
    vendas_salvas.extend(vendas)
    return {"total_recebido": len(vendas)}

@app.get("/vendas")
def listar_vendas():
    return vendas_salvas


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:3000"] se quiser restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
