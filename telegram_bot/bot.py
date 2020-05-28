from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram_bot import magic_api

updater = Updater(token='1156666119:AAETH8I5jJJYoe9JUQIXC7QVpjRyq0Q1Dx0', use_context=True)

dispatcher = updater.dispatcher #intermediador entre a cozinha e o garçom

def start_func(update, context):       #receita
    context.bot.send_message(chat_id=update.effective_chat.id, text="Jarbas_bot iniciado!")


def hello_func(update, context):       #receita
    context.bot.send_message(chat_id=update.effective_chat.id, text="Falaee Cacaroto!")


def find_func(update, context): #receita
    card_name = ' '.join(context.args)
    image_url = magic_api.get_card_image_url_by_name(card_name)
    oracle_text = magic_api.get_card_oracle_text_by_name(card_name)
    context.bot.send_photo(update.effective_chat.id, image_url, f'Oracle text: {oracle_text}')  #Dono do Restaurante - Sabe tudo!!!



start_handler = CommandHandler('start', start_func) #Cozinheiro
find_handler = CommandHandler('find', find_func)    #Cozinheiro
hello_handler = CommandHandler('hello', hello_func) #Cozinheiro
dispatcher.add_handler(start_handler)   #Garçom
dispatcher.add_handler(hello_handler)   #Garçom
dispatcher.add_handler(find_handler)    #Garçom


updater.start_polling()  #polling == ação repetida de tempos em tempos