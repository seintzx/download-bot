#!/usr/bin/env python3

from subprocess import PIPE, Popen


def run_cmd(command):
    result = Popen(args=command, stdout=PIPE, stderr=PIPE, shell=True)
    return result.communicate()[0]
