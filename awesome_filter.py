from telegram.ext import BaseFilter
#El filtro pasa todos los mensajes a minúsculas
class AwesomeFilter(BaseFilter):
    def filter(self, message):
        if message.text:
            return message.text.lower()