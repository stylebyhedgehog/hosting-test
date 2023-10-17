import time

from flask import Flask, request

import telebot

TOKEN = "6423402186:AAF5J0RrcoNO7xOMkjxQfZKn7aQdQ0IPxr0"
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    time.sleep(4)
    print(message)
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    print(json_str)
    update = telebot.types.Update.de_json(json_str)
    print("AAAA",update)
    bot.process_new_updates([update])
    return '', 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://test-host-h6po.onrender.com/' + TOKEN)
    return "!", 200

