#importa a conexão criada
from conexao import get_conexao

#importa a biblioteca psycog2
from psycopg2.extras import RealDictCursor

# Importa o jsonfy do flask para retornas os dados no formato json
from flask import jsonify

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, nome, descricao FROM tarefas;"
    )
    # Busca todos os registros na tabela
    tarefas = cursor.fetchall()

    # Fecha as conexões
    cursor.close()
    conn.close()

    return jsonify(tarefas)