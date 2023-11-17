from fastapi import FastAPI, HTTPException, Depends, APIRouter
import sqlite3
from typing import Optional

app = FastAPI()
router = APIRouter()

# Função para obter a conexão com o banco de dados
def obter_conexao():
    conexao = sqlite3.connect('meu_banco_de_dados.db')
    return conexao

# Rota para obter informações do banco de dados
@app.get("/dados/{cpf_ou_cnpj}")
def obter_cpf_cnpj(cpf_ou_cnpj: int, conexao: sqlite3.Connection = Depends(obter_conexao)):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM meus_dados WHERE cpf_ou_cnpj=?", (cpf_ou_cnpj,))
    dados = cursor.fetchone()

    if dados is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    return {"dados": dados}


@app.get("/por_nome/{nome}")
def obter_cpf_cnpj(nome: str, conexao: sqlite3.Connection = Depends(obter_conexao)):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM meus_dados WHERE nome LIKE ?", ("%" + nome + "%",))
    dados = cursor.fetchone()

    if dados is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"dados": dados}

app.include_router(router)

