from django.core.management import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram_bot.views import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        updater = Updater('5028779716:AAEWI_822MoMa8GKg2wADRNKkTBvI0eujA4')
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, received_msg))
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact))
        updater.start_polling()
        updater.idle()

