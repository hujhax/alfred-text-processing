#!/usr/bin/python
# -*- coding: utf-8 -*-

from ProcessSelection import setClipboardData, sendPasteKey, \
                             processSelectedString, sendLefts


def twiddle(text):
    setClipboardData(text[::-1])
    sendPasteKey()


sendLefts(2, True)
processSelectedString(twiddle)
