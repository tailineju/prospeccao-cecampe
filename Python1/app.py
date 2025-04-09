from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Carregar dados do Excel
def carregar_dados():
    return pd.read_excel("escolas.xlsx")

# Salvar dados no Excel
def salvar_dados(df):
    df.to_excel("escolas.xlsx", index=False)

@app.route("/")
def index():
    dados = carregar_dados()
    return render_template("index.html", dados=dados)

@app.route("/buscar", methods=["POST"])
def buscar():
    codigo = request.form.get("codigo")
    dados = carregar_dados()
    escola = dados[dados["codigo_escola"] == int(codigo)]
    if not escola.empty:
        return render_template("index.html", dados=dados, escola=escola.iloc[0])
    return render_template("index.html", dados=dados, erro="Escola não encontrada.")

@app.route("/atualizar", methods=["POST"])
def atualizar():
    codigo = request.form.get("codigo")
    novo_status = request.form.get("status")
    dados = carregar_dados()
    dados.loc[dados["codigo_escola"] == int(codigo), "status"] = novo_status
    salvar_dados(dados)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)