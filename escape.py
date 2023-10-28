from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route('/<ruc_cliente>')
def ver_ruc_cliente(ruc_cliente):
    ruc_cliente = '45-55'
    return f"el RUC es: {escape(ruc_cliente)}!"


