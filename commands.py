from telegram import (InlineKeyboardButton,
                      InlineKeyboardMarkup)
from random import randint#genera un entero aleatorio
import procesar_html
import pelicula

def alarm(bot, job):
    bot.send_message(job.context, text='Beep!')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Bienvenido/a! Introduce el título de una película o serie y te recomendaré si puedes verla \ "
                                                          "o si pierdes completamente tu valioso tiempo...")

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def chat_id(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='El idenficador de este chat es ' + str(update.message.chat_id))

def inline_keyboard(bot, update):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],
                [InlineKeyboardButton("Option 3", callback_data='3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def set_timer(bot, update, args, job_queue, chat_data):
    chat_id = update.message.chat_id
    try:
        due = int(args[0])
        if due < 0:
            update.message.reply_text('Sorry we can not go back to future!')
            return

        job = job_queue.run_repeating(alarm, due, context=chat_id)
        chat_data['job'] = job

        update.message.reply_text('Timer successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')

def unset(bot, update, chat_data):
    if 'job' not in chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Timer successfully unset!')

def python(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='🐍🐍🐍🐍🐍🐍')
def buscapeli(bot,update,chat_data):
    if update.message.text == '/buscapeli':
        bot.send_message(chat_id=update.message.chat_id,
                         text="Introduce el título o palabras claves del título de la peli/serie de la siguiente forma:\n"
    
                              "/buscapeli El laberinto del fauno ")

    else:
        #bot.send_message(chat_id=update.message.chat_id,text="Palabras buscadas:"+ update.message.text[10:])
        imprimir_pelis(bot,update)
        #inline_keyboard(bot,update)
def imprimir_pelis(bot,update):
    #string = procesar_html.busqueda(update.message.text[10:])
    seleccionar_pelicula(bot,update)

def seleccionar_pelicula(bot, update):
    for pelis in  procesar_html.busqueda(update.message.text[10:]):
        #bot.send_message(chat_id=update.message.chat_id, parse_mode='HTML', text="<img itemprop='image' width='160' height='231' src='https://pics.filmaffinity.com/airbag-110139764-mmed.jpg'>")
        #bot.send_message(chat_id=update.message.chat_id, parse_mode='HTML', text="<a href='"+str(pelis.url)+"'></a>")
        bot.send_message(chat_id=update.message.chat_id, text=pelis.titulo + " " + pelis.year )
