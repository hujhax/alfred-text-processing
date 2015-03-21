#!/usr/bin/python
# -*- coding: latin-1 -*-

from ProcessSelection import setClipboardData, sendPasteKey, \
                             processSelectedString


def hyphenateText(text):
    setClipboardData(text.replace(" ", "-"))
    sendPasteKey()


processSelectedString(hyphenateText)
