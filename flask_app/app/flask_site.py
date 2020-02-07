from flask import Flask, render_template
import bot_telegram.telegram_bot as t_bot

# Instancia o flask
app = Flask(__name__)

# Esse método serve apenas para mostrar que o bot está em execução
@app.route('/')
@app.route('/index')
def index():
    """
    Retorna a página inicial do flask
    """
    return render_template('index.html', title='Bot de Rastreio')

