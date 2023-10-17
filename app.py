import logging
import time

import flask
# import os
# import telebot
from flask_cors import CORS
logging.info('App start')
# API_TOKEN = os.environ.get("TELEBOT_TOKEN")

# WEBHOOK_HOST = os.environ.get("HOST_URL")
WEBHOOK_PORT = 80  # 443, 80, 88 or 8443 (port need to be 'open')
# WEBHOOK_LISTEN = os.environ.get("IP")  # In some VPS you may need to put here the IP addr
#
# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)
#
# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)
#
# bot = telebot.TeleBot(API_TOKEN)

app = flask.Flask(__name__)

print("Start")
# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'hello'


@app.route("/test-messaging", methods=['POST'])
def testhook():
    if flask.request.headers.get('content-type') == 'application/json':
        return str(flask.request.get_data())
    else:
        flask.abort(403)

# Process webhook calls
# @app.route(WEBHOOK_URL_PATH, methods=['POST'])
# def webhook():
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)


# @app.route("/test-messaging", methods=['POST'])
# def testhook():
#     if flask.request.headers.get('content-type') == 'application/json':
#         bot.send_message(5891891154, str(flask.request.get_data()))
#         return ''
#     else:
#         flask.abort(403)

# Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message,
#                  ("Hi there"))


# Handle all other messages
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message, message.text)
#
#
# # Remove webhook, it fails sometimes the set if there is a previous webhook
# bot.remove_webhook()
#
# time.sleep(1)
#
# # Set webhook
# bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
#                 # certificate=open(WEBHOOK_SSL_CERT, 'r')

if __name__ == "__main__":
    app.run(port=80)
        # host=WEBHOOK_LISTEN,
        # ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
