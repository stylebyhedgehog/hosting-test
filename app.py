# import logging
# import time
#
# import flask
# # import os
# import telebot
# # from flask_cors import CORS
# logging.info('App start')
# API_TOKEN =  "6423402186:AAF5J0RrcoNO7xOMkjxQfZKn7aQdQ0IPxr0" #os.environ.get("TELEBOT_TOKEN")
#
# WEBHOOK_HOST = "https://test-host-h6po.onrender.com/"
# WEBHOOK_PORT = 80  # 443, 80, 88 or 8443 (port need to be 'open')
# # WEBHOOK_LISTEN = os.environ.get("IP")  # In some VPS you may need to put here the IP addr
# #
# WEBHOOK_URL_BASE = WEBHOOK_HOST #"https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL = WEBHOOK_HOST+API_TOKEN
#
# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)
#
# bot = telebot.TeleBot(API_TOKEN)
#
# app = flask.Flask(__name__)
#
# print("Start")
# # Empty webserver index, return nothing, just http 200
# @app.route('/', methods=['GET', 'HEAD'])
# def index():
#     return 'hello'
#
#
# @app.route("/test-post", methods=['POST'])
# def testpost():
#     if flask.request.headers.get('content-type') == 'application/json':
#         return str(flask.request.get_data())
#     else:
#         flask.abort(403)
#
# # Process webhook calls
# @app.route("/"+API_TOKEN, methods=['POST'])
# def webhook():
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)
#
#
# @app.route("/test-messaging", methods=['POST'])
# def testhook():
#     if flask.request.headers.get('content-type') == 'application/json':
#         bot.send_message(5891891154, str(flask.request.get_data()))
#         return ''
#     else:
#         flask.abort(403)
#
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message,
#                  ("Hi there"))
#
#
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message, message.text)
#
#
# bot.remove_webhook()
#
# time.sleep(1)
#
# # Set webhook
# bot.set_webhook(url=WEBHOOK_URL)
import json
import os

from flask import Flask, request

import telebot

TOKEN = "6423402186:AAF5J0RrcoNO7xOMkjxQfZKn7aQdQ0IPxr0"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    print(json_string)
    update = telebot.types.Update.de_json(json_string)

    if 'message' in json_string:
        message = telebot.types.Message.de_json(json.loads(json_string)['message'])
        if message.text == '/start':
            start(message)
        else:
            bot.process_new_updates([update])

    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://test-host-h6po.onrender.com/' + TOKEN)
    return "!", 200

