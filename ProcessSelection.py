#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os


def getClipboardData():
    env = os.environ.copy()
    env['LC_CTYPE'] = 'UTF-8'

    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE, env=env)
    p.wait()
    data = p.stdout.read()
    return data


def setClipboardData(data):
    env = os.environ.copy()
    env['LC_CTYPE'] = 'UTF-8'

    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, env=env)
    p.stdin.write(data)
    p.stdin.close()
    p.wait()


def sendKeyCore(keyText):
    command1 = "osascript -e 'tell application "
    command2 = '"System Events" to ' + keyText + "'"
    os.system(command1 + command2)


def sendKey(key):
    return sendKeyCore('keystroke "' + key + '"')


def sendCommandKey(key):
    return sendKeyCore('keystroke "' + key + '" using {command down}')


def sendLefts(numLefts, shift=False):
    if shift:
        keyText = "key code 123 using {shift down}"
    else:
        keyText = "key code 123"
    for _ in xrange(numLefts):
        sendKeyCore(keyText)


def commandDelay():
    os.system("osascript -e 'delay 0'")


def sendCopyKey():
    sendCommandKey("c")
    commandDelay()


def sendPasteKey():
    sendCommandKey("v")
    commandDelay()


def doNothing():
    pass


def processSelectedString(onStringSelection, onEmptySelection=doNothing):
    savedClipboard = getClipboardData()
    sentinel = "§"
    setClipboardData(sentinel)
    sendCopyKey()
    text = getClipboardData()
    if text == sentinel:
        onEmptySelection()
    else:
        onStringSelection(text)
    setClipboardData(savedClipboard)
