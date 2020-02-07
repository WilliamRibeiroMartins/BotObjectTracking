import time

from bot_telegram import telegram_bot
from flask_app.app import flask_site

#Mantem o programa sendo executado
print("Iniciando o bot...")
print("Bot iniciado")

# Iniciando o bot
telegram_bot.start_bot()

# Iniciando o flask
flask_site.app.run()

