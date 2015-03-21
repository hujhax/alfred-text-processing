#!/usr/bin/python
# -*- coding: latin-1 -*-

import subprocess
import os


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    p.wait()
    data = p.stdout.read()
    return data


def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
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


def sendKeyCode(keyCode):
    return sendKeyCore('key code "' + str(keyCode) + '"')


def commandDelay():
    os.system("osascript -e 'delay 0'")


def sendCopyKey():
    sendCommandKey("c")
    commandDelay()


def sendPasteKey():
    sendCommandKey("v")
    commandDelay()


def processSelectedString(onStringSelection, onEmptySelection):
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
