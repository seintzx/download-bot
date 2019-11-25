#!/usr/bin/env python3
"""
move elif cascade from main here

function that return a dictionary with 2 elements:
    1) cmd to run
    2) message to send

def check_command(command):
    if
    elif
    elif
    ...

    return dic
"""


def run_cmd(command):
    mess = ""
    cmd = ""

    if command == '/hi':
        telegram_bot.sendMessage(chat_id, str("Hi! I'm your new Assistant"))

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


    bot_msg = {'mess': mess, 'cmd': cmd}
    return (bot_msg)
