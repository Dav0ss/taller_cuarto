from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hello word'

@app.route('/tituloh2')
def tituloh2():
    return '<h2>Esto es un titulo HTML</h2>'

@app.route('/parrafo')
def parrafo():
    return '<p>Esto es un parrafo</p>'

@app.route('/get-lista')
def lista():
    return [
        "administrador de sistemas",
        "secretaria",
        "gerente",
        "vendedor",
        "auxiliar de compra"
    ]
@app.route('/get-diccionario')
def diccionario():
    dicc1 = {
        "apellidos" : "rojas",
        "edad" : 64,
        "fechanac" : "1960-06-01",
        "id" : 36,
        "nombres" : "Justo"
    }
    dicc2 = {
        "apellidos" : "rojas",
        "edad" : 64,
        "fechanac" : "1960-06-01",
        "id" : 36,
        "nombres" : "Justo"
    }
    
    return [dicc1, dicc2]


    
























