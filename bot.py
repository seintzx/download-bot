#!/usr/bin/env python3

from telepot.loop import MessageLoop
import botterino
import configuration
import os
import sys
import telepot
import time, datetime


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].split('@')[0]

    # Filter away undesirable users
    if chat_id not in users:
        return

    print("In chat with " + str(chat_id))
    print("Received: {0}".format(command))

    telegram_bot.sendMessage(chat_id, botterino.run_cmd(command))


if __name__ == "__main__":
    now = datetime.datetime.now()
    users = [
        int(user) for user in configuration.get_config()['user'].split(',')
    ]
    token = str(configuration.get_config()['token'])

    telegram_bot = telepot.Bot(token)
    MessageLoop(telegram_bot, action).run_as_thread()

    print('Up and Running....')
    while 1:
        time.sleep(10)
