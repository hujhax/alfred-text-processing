#!/usr/bin/python
# -*- coding: latin-1 -*-

from ProcessSelection import setClipboardData, sendPasteKey, \
                             processSelectedString, sendLefts
from functools import partial
import argparse
import re


def outputTags(beginTag, endTag):
    setClipboardData(beginTag + endTag)
    sendPasteKey()
    sendLefts(len(endTag.decode('utf-8')))


def surroundWithTags(beginTag, endTag, text):
    trimmer = re.compile("^(\s*)(.*[^\s])(\s*)$")
    matches = trimmer.match(text)
    setClipboardData(matches.group(1) + beginTag + matches.group(2)
                     + endTag + matches.group(3))
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
