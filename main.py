from flask import Flask
from tarefa import buscar_tarefas

app = Flask(__name__)
@app.route("/api")
def index():
    return "Api rodando"

#retorno
@app.route("/api/tarefas")
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas


if __name__ == "__main__":
    app.run(debug=True)