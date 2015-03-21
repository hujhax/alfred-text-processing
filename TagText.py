#!/usr/bin/python
# -*- coding: latin-1 -*-

from ProcessSelection import setClipboardData, sendPasteKey, \
                             processSelectedString
from functools import partial
import argparse


def outputTags(beginTag, endTag):
    setClipboardData(beginTag + endTag)
    sendPasteKey()


def surroundWithTags(beginTag, endTag, text):
    setClipboardData(beginTag + text + endTag)
    sendPasteKey()


def handleTags(beginTag, endTag):
    processSelectedString(partial(surroundWithTags, beginTag, endTag),
                          partial(outputTags, beginTag, endTag))


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
