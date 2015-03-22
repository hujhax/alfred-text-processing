#!/usr/bin/python
# -*- coding: latin-1 -*-

from ProcessSelection import setClipboardData, sendPasteKey, \
                             processSelectedString
import argparse


def hyphenateText(text):
    setClipboardData(text.replace(" ", "-"))
    sendPasteKey()


def hashtagText(text):
    textNoSpace = "".join(text.split())
    hashtag = "#" + textNoSpace.lower()
    setClipboardData(hashtag)
    sendPasteKey()


def parseArguments():
    toolDescription = "A few functionalities for altering "\
                      "the selected text."

    parser = argparse.ArgumentParser(description=toolDescription)
    behaviors = parser.add_mutually_exclusive_group()
    behaviors.add_argument("--hyphenate", action="store_true",
                           help="Replace spaces with hyphens.")
    behaviors.add_argument("--hashtag", action="store_true",
                           help="Convert the string to a hashtag, #likethis.")
    return parser.parse_args()


args = parseArguments()


if args.hyphenate:
    processSelectedString(hyphenateText)
elif args.hashtag:
    processSelectedString(hashtagText)
