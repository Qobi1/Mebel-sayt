from django.shortcuts import render
from telegram.ext import CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
# Create your views here.
from app1.models import Category
from .models import *


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    try:
        user_info = User.objects.get(user_id=user.id)
        log_info = Log.objects.get(user_id=user.id)
        state = log_info.log['state']
        name = user_info.name
        update.message.reply_text(f'Assalomu alaykum {name}', reply_markup=buttons(type='ctg'))
        log_info.log['state'] = state
        log_info.save()
        print(state)
    except:
        user_info = None
        log_info = Log()
    if user_info is None:
        log_info.log = {'state': 1}
        log_info.user_id = user.id
        log_info.save()
        update.message.reply_text('Assalomu alaykum, Ismingizni kriting')


def received_msg(update: Update, context: CallbackContext):
    msg = update.message.text
    user = update.effective_user
    try:
        user_info = User.objects.get(user_id=user.id)
    except:
        user_info = User()

    log = Log.objects.get(user_id=user.id)
    get_log = log.log
    state = get_log.get('state')
    if state == 1:
        get_log['state'] = 2
        user_info.name = msg
        user_info.user_id = user.id
        user_info.save()
        update.message.reply_text("Familiyangizni kriting")
        log.save()
    elif state == 2:
        get_log['state'] = 3
        user_info.surname = msg
        user_info.user_id = user.id
        user_info.save()
        log.save()
        update.message.reply_text('Raqamingizni kriting', reply_markup=buttons(type='phone_number'))
    elif state == 3:
        update.message.reply_text('Raqamni kritish tugmasini bosing')


def contact(update: Update, context: CallbackContext):
    user = update.effective_user
    contact = update.message.contact
    user_info = User.objects.get(user_id=user.id)
    log_info = Log.objects.get(user_id=user.id)
    log = log_info.log
    state = log.get('state', 0)
    if state == 3:
        log['state'] = 4
        user_info.phone_number = contact.phone_number
        user_info.user_id = user.id
        user_info.save()
        log_info.save()
        update.message.reply_text('Menudan brini tanlang!', reply_markup=buttons(type='ctg'))


def buttons(type=None):
    btn = []
    if type == 'phone_number':
        btn = [[KeyboardButton('Raqamni kritish', request_contact=True)]]
    elif type == 'ctg':
        ctg = Category.objects.all()
        for i in range(0, len(ctg) - 1, 2):
            btn.append([KeyboardButton(ctg[i].content), KeyboardButton(ctg[i+1].content)])
        if len(ctg) % 2 != 0:
            btn.append([KeyboardButton(ctg[len(ctg) - 1].content)])
    else:
        pass
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)
