from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

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
    return {"total_recebido": len(vendas)}
