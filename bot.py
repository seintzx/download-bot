#!/usr/bin/env python3

from telepot.loop import MessageLoop
import commander
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

    if command == '/hi':
        telegram_bot.sendMessage(chat_id, str("Hi! I'm Daniele's Assistant"))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id,
                                 str(now.hour) + str(":") + str(now.minute))
    elif command == '/troff':
        commander.run_cmd('sudo service transmission-daemon stop')
        telegram_bot.sendMessage(chat_id, str('transmission stopped!'))
    elif command == '/tron':
        commander.run_cmd('sudo service transmission-daemon start')
        telegram_bot.sendMessage(chat_id, str('transmission started!'))
    elif command == '/minirst':
        commander.run_cmd('sudo service minidlna force-reload')
        telegram_bot.sendMessage(chat_id, str('minidlna restarted!'))
    elif command.split(' ')[0] == '/tradd':
        magnet = command.split(' ')[1]
        telegram_bot.sendMessage(chat_id,
                                 str('Adding "' + magnet + '" to dowloads'))
        commander.run_cmd(
            'transmission-remote --auth transmission:transmission -a "' +
            magnet + '"')
        telegram_bot.sendMessage(chat_id, str('Torrent added to downloads!'))
    elif command == '/trlist':
        trlist = commander.run_cmd(
            'transmission-remote --auth transmission:transmission -l')
        telegram_bot.sendMessage(chat_id, trlist)
    elif command == '/top10ps':
        top10ps = commander.run_cmd(
            'ps -ax --sort=-pcpu -o user,pid,%cpu,%mem,start,time,cmd | head -n 10'
        )
        telegram_bot.sendMessage(chat_id, top10ps)
    elif command == '/avail':
        df_sda1 = commander.run_cmd('df -h /dev/sda1')
        telegram_bot.sendMessage(chat_id, df_sda1)


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
