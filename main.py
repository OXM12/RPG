from email import message
from mimetypes import types_map
from msilib.schema import AdminExecuteSequence
from pyexpat import model
import re
from subprocess import call
import telebot
from telebot import types


bot = telebot.TeleBot("5479511126:AAE0fRbBFcKKN5bJF8H-m73FKqEe5oVdRck", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    global bugdoy
    global mol
    global qoy
    global tovuq 
    tanga = 100
    olmos = 0
    
    mol = 1
    qoy = 1
    tovuq = 1
    bugdoy = 100
    
    menu_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ferma = types.KeyboardButton("Ferma🏡")
    bozor = types.KeyboardButton("Bozor💰")
    info = types.KeyboardButton("Infoℹ")
    menu_button.add(ferma, bozor, info)
    bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}. \n Quvnoq ferma o'yiniga hush kelibsiz!", reply_markup=menu_button)

@bot.message_handler()
def menu(message):
    if message.text == "Ferma🏡":
        ferma_menu = types.InlineKeyboardMarkup(row_width=2)
        hayvonlar = types.InlineKeyboardButton("Hayvonlar🐓", callback_data="hayvonlar")
        daraja = types.InlineKeyboardButton("Ferma darajasi📈", callback_data="daraja")
        binolar = types.InlineKeyboardButton("Binolar🏚", callback_data="binolar")
        ferma_menu.add(hayvonlar, daraja, binolar)
        bot.send_message(message.chat.id, f"Fermaga hush kelibsiz, kerakli tugmani tanlang:", reply_markup=ferma_menu)


    elif message.text == "Bozor💰":
        bozor_menu = types.InlineKeyboardMarkup(row_width=2)
        valyuta = types.InlineKeyboardButton("Valyuta💎", callback_data="valyuta")
        hayvon = types.InlineKeyboardButton("Hayvon olish/sotish🐄", callback_data="hayvon")
        yemish = types.InlineKeyboardButton("yemish olish🌾", callback_data="yemish")
        bozor_menu.add(valyuta,hayvon,yemish)
        bot.send_message(message.chat.id, "Bozorga hush kelibsiz", reply_markup=bozor_menu)
    elif message.text == "Infoℹ":
        info_menu = types.InlineKeyboardMarkup(row_width=2)
        admin = types.InlineKeyboardButton("Admin👨‍💻", url="t.me/ozodbek_khayrullaev")
        kanal = types.InlineKeyboardButton("Kanal📢", url="t.me/execodemylife")
        info_menu.add(admin, kanal)
        bot.send_message(message.chat.id, "Infoga hush kelibsiz", reply_markup=info_menu)
        
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    global mol
    mol = 1
    qoy = 1
    tovuq = 1
    bugdoy = 100
    hayvonlar_menu = types.InlineKeyboardMarkup(row_width=2)
    boqish = types.InlineKeyboardButton("Boqish🌾", callback_data="boqish")
    hosil = types.InlineKeyboardButton("Hosil olish🥩", callback_data="hosil")
    ortga = types.InlineKeyboardButton("Ortga⬅", callback_data="menu")
    hayvonlar_menu.add(boqish, hosil, ortga)
    if call.message:
        if call.data == "hayvonlar":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= f"Hayvonlaringiz soni:\nMol: {mol}\nQo'ylar: {qoy}\nTovuqlar: {tovuq}", reply_markup=hayvonlar_menu)
        elif call.data == "boqish":
            if bugdoy > 9:
                bugdoy -= 10
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= f"Hayvonlaringizni boqdingiz\nQolgan bug'doy: {bugdoy}")
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= f"Bug'doyingiz kam")
        elif call.data == "hosil":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= f"Hosil yig'ib olindi")
bot.infinity_polling()