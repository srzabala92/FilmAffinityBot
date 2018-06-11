import telegram
import procesar_html as html
import unicodedata
import telegram
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,
                          InlineQueryHandler,
                          CallbackQueryHandler)
import logging
from awesome_filter import AwesomeFilter
import commands
import messages
import utils

def main():
    #INICIALIZAR BOT
    t_bot = telegram.Bot(token="533616434:AAF8QHIFYwS5LuGV6RRR7cUq_Ymzl4d4SGU")
    print(t_bot.get_me())

    updater = Updater(token="533616434:AAF8QHIFYwS5LuGV6RRR7cUq_Ymzl4d4SGU")
    dispatcher = updater.dispatcher
    # commands handlers
    start_command_handler = CommandHandler('start', commands.start)
    busca_peli_command_handler = CommandHandler('buscapeli', commands.buscapeli,pass_chat_data=True)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(busca_peli_command_handler)
    updater.start_polling()
if __name__ == "__main__":
    main()