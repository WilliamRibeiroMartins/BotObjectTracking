from telegram.ext.filters import Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler
from rastreamento.tracking import Tracking

import logging, time

#Bot Token
BOT_TOKEN = '1001294837:AAGpxUAUJfosdvklkN9ZszYCM_lTADsh9TM'

updater = Updater(token=BOT_TOKEN)

#Cria os handle's (comandos)
dispatcher = updater.dispatcher

#Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    """
    Inicia o bot
    """
    try:
        logger.info("Chamando o método 'start'")
        msg = f"Olá, Eu sou o {bot.name}. Informe o código do objeto que você deseja rastrear"
        
        # Envia a mensagem para o usuário
        bot.send_message(chat_id=update.message.chat_id, text=msg)
    except Exception as ex:
        error(bot, update, ex)

def track(bot, update, args):
    """
    Realiza o rastreamento da encomenda
    """
    try:
        logger.info("Chamando o método 'track'")

        # É feito o rastreamento de cada código informado
        for code in args:
            object_tracking = Tracking()
            places = object_tracking.track(code)
            order = ''

            # Concatena as atualiações feitas na encomenda para enviar somente uma mensagem
            for place in places:
                order = f'{order} \n {place} \n ==========================='

            # Envia a mensagem para o usuário
            bot.send_message(chat_id=update.message.chat_id, text=order)
    except Exception as ex:
        error(bot, update, ex)
    
def stop(bot, update):
    """
    Encerra o bot
    """
    try:
        logger.info("Chamando o método 'stop'")
        msg = 'Encerrando... Tchau'
        
        # Envia a mensagem para o usuário
        bot.send_message(chat_id=update.message.chat_id, text=msg)
    except Exception as ex:
        error(bot, update, ex)

def help(bot, update):
    """
    Exibe os comandos disponíveis
    """
    try:
        logger.info("Chamando o método 'help'")
        msg = '/start - Inicia o bot\n /stop - Finaliza o bot \n /track - Mostra o estado da encomenda (É necessário informar o código do objeto na frente do comando Ex: /track BR1235) \n /help - Mostra os comandos disponíveis'
        
        # Envia a mensagem para o usuário
        bot.send_message(chat_id=update.message.chat_id, text=msg)
    except Exception as ex:
        error(bot, update, ex)

def error(bot, update, ex):
    """
    Retorna a mensagem de erro
    """
    msg_log = 'Error: {}'.format(ex)
    msg_bot = 'Desculpe, a operação não pode ser realizada'

    # Envia a mensagem para o usuário
    bot.send_message(chat_id=update.message.chat_id, text=msg_bot)
    
    logger.exception(msg_log)

#Define os comandos
start_handle = CommandHandler('start', start)
dispatcher.add_handler(start_handle)

stop_handle = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handle)

track_handle = CommandHandler('track', track, pass_args=True)
dispatcher.add_handler(track_handle)

help_handle = CommandHandler('help', help)
dispatcher.add_handler(help_handle)

#Inicia o bot
updater.start_polling()
