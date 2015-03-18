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


def sendCommandKey(key):
    command1 = "osascript -e 'tell application "
    command2 = '"System Events" to keystroke "' + key + '"'
    command3 = " using {command down}'"

    os.system(command1 + command2 + command3)


def commandDelay():
    os.system("osascript -e 'delay 0'")


def sendCopyKey():
    sendCommandKey("c")
    commandDelay()


def sendPasteKey():
    sendCommandKey("v")
    commandDelay()


def sendAsterisks():
    setClipboardData("**")
    sendPasteKey()


def surroundWithAsterisks(text):
    setClipboardData("*" + text + "*")
    sendPasteKey()


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

processSelectedString(surroundWithAsterisks, sendAsterisks)
