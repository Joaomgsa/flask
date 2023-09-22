from flask import Flask, render_template


app = Flask(__name__)


# criar primeira pagina
# route ->caminho
# funcao -> o que voce quer exibir na pagina
# 
@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/indicadores")
def contatos():
    return render_template("indicadores.html")

# colocar site no ar 
if __name__ == "__main__":
    app.run(debug=True)