from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/ciudad')
def get_ciudad():
    return render_template('ciudades.html')