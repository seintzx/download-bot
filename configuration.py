#!/usr/bin/env python3

import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("config.txt")
    user = config.get("configuration", "user")
    token = config.get("configuration", "token")
    conf = {'user': user, 'token': token}
    return (conf)
