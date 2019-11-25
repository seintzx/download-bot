#!/usr/bin/env python3

import commander


def run_cmd(command):
    mess = ""

    if command == '/hi':
        mess = "Hi! I'm your new Assistant"
    elif command == '/date':
        mess = commander.run_cmd('date')
    elif command == '/troff':
        commander.run_cmd('sudo service transmission-daemon stop')
        mess = 'transmission stopped!'
    elif command == '/tron':
        commander.run_cmd('sudo service transmission-daemon start')
        mess = 'transmission started!'
    elif command == '/minirst':
        commander.run_cmd('sudo service minidlna force-reload')
        mess = 'minidlna restarted!'
    elif command.split(' ')[0] == '/tradd':
        magnet = command.split(' ')[1]
        commander.run_cmd(
            'transmission-remote --auth transmission:transmission -a "' +
            magnet + '"')
        mess = 'Torrent added to downloads!'
    elif command == '/trlist':
        mess = commander.run_cmd(
            'transmission-remote --auth transmission:transmission -l')
    elif command == '/top10ps':
        mess = commander.run_cmd(
            'ps -ax --sort=-pcpu -o user,pid,%cpu,%mem,start,time,cmd | head -n 10'
        )

    return (mess)
