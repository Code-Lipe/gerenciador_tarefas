# Importa as classes
from flask import Flask, render_template, request, redirect, url_for

# Cria a aplicação Flask
app = Flask(__name__)

# Lista para armazenar tarefas (em memória)
tasks = []

# Define a primeira rota da aplicação
# '/' significa a página inicial (home)
@app.route("/")
def home():
    # Passa a lista de tarefas para template
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    # Pega o dado do formulário (campo 'task')
    task = request.form.get("task")

    if task:
        tasks.append(task) # Adiciona a lista
    return redirect(url_for("home")) # Redireciona para a home para atualizar a lista

@app.route("/delete/<int:task_index>")
def delete_task(task_index):
    try:
        # tentar remover a tarefa pelo índice recebido na URL
        tasks.pop(task_index)
    except IndexError:
        # Caso o índice não exista, apenas ignora
        pass
    # Após a exclusão, redireciona para a página inicial para atualizar
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
