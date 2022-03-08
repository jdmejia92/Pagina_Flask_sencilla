from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def la_funcion():
    return render_template("mipagina.html")

@app.route("/bye/<nombre>/<apellido>")
def otra_funcion(nombre, apellido):
    return render_template("despedida.html", name=nombre, surname=apellido)
    return f"hasta luego {nombre} {apellido}"