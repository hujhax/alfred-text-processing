#!/usr/bin/python
# -*- coding: latin-1 -*-

import subprocess
import os
from functools import partial
import argparse

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


def outputTags(beginTag, endTag):
    setClipboardData(beginTag + endTag)
    sendPasteKey()


def surroundWithTags(beginTag, endTag, text):
    setClipboardData(beginTag + text + endTag)
    sendPasteKey()


def handleTags(beginTag, endTag):
    processSelectedString(partial(surroundWithTags, beginTag, endTag),
                          partial(outputTags, beginTag, endTag))


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


def parseArguments():
    toolDescription = "Adds prefix/postfix to selected text,"\
                      " or outputs those tags and allows the"\
                      " user to type in between them."

    parser = argparse.ArgumentParser(description=toolDescription)
    parser.add_argument("beginTag", help="The opening tag.")
    parser.add_argument("endTag", help="The closing tag.")
    return parser.parse_args()


args = parseArguments()
handleTags(args.beginTag, args.endTag)
