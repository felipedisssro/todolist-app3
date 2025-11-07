import psycopg2

# Função que retorna a conexão com o banco de dados portgres
def get_conexao():
    conn = psycopg2.connect (
        dbname ='todolist',
        user ='postgres',
        password='postgres',
        host='127.0.0.1',
        port=5432
    )
    return conn