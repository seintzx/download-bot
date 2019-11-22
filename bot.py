#!/usr/bin/env python3

from subprocess import PIPE, Popen
from telepot.loop import MessageLoop
import configuration
import os
import sys
import telepot
import time, datetime

now = datetime.datetime.now()

# users = []
# for user in configuration.get_config()['user'].split(','):
#     users.append(int(user))
# print(users)

users = [int(user) for user in configuration.get_config()['user'].split(',')]


def out(command):
    result = Popen(args=command, stdout=PIPE, stderr=PIPE, shell=True)
    return result.communicate()[0]


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].split('@')[0]

    # Filter away undesirable users
    if chat_id not in users:
        return

    print("In chat with " + str(chat_id))
    print("Received: {0}".format(command))

    token = str(configuration.get_config()['token'])
    telegram_bot = telepot.Bot(token)

    if command == '/hi':
        telegram_bot.sendMessage(chat_id, str("Hi! I'm Daniele's Assistant"))
    # elif command == '/time':
    #     telegram_bot.sendMessage(chat_id,
    #                              str(now.hour) + str(":") + str(now.minute))
    # elif command == '/troff':
    #     out('sudo service transmission-daemon stop')
    #     telegram_bot.sendMessage(chat_id, str('transmission stopped!'))
    # elif command == '/tron':
    #     out('sudo service transmission-daemon start')
    #     telegram_bot.sendMessage(chat_id, str('transmission started!'))
    # elif command == '/minirst':
    #     out('sudo service minidlna force-reload')
    #     telegram_bot.sendMessage(chat_id, str('minidlna restarted!'))
    # elif command.split(' ')[0] == '/tradd':
    #     magnet = command.split(' ')[1]
    #     telegram_bot.sendMessage(chat_id,
    #                              str('Adding "' + magnet + '" to dowloads'))
    #     out('transmission-remote --auth transmission:transmission -a "' +
    #         magnet + '"')  # -w /mnt/fastgate/Data')
    #     telegram_bot.sendMessage(chat_id, str('Torrent added to downloads!'))
    # elif command == '/trlist':
    #     trlist = out('transmission-remote --auth transmission:transmission -l')
    #     telegram_bot.sendMessage(chat_id, trlist)
    # elif command == '/top10ps':
    #     top10ps = out(
    #         'sudo ps -ax --sort=-pcpu -o user,pid,%cpu,%mem,start,time,cmd | head -n 10'
    #     )
    #     telegram_bot.sendMessage(chat_id, top10ps)
    # elif command == '/avail':
    #     df_sda1 = out('df -h /dev/sda1')
    #     telegram_bot.sendMessage(chat_id, df_sda1)


def main():
    token = str(configuration.get_config()['token'])
    telegram_bot = telepot.Bot(token)

    # print(telegram_bot.getMe())

    MessageLoop(telegram_bot, action).run_as_thread()
    print('Up and Running....')

    while 1:
        time.sleep(10)


if __name__ == "__main__":
    main()
