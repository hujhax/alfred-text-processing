#!/usr/bin/python
# -*- coding: latin-1 -*-

from ProcessSelection import setClipboardData, sendPasteKey, \
                             processSelectedString
import argparse


def upperText(text):
    setClipboardData(text.upper())
    sendPasteKey()


def lowerText(text):
    setClipboardData(text.lower())
    sendPasteKey()


def toggleText(text):
    prevText = text
    text = text.upper()
    if text == prevText:
        text = text.lower()
    setClipboardData(text)
    sendPasteKey()


def parseArguments():
    toolDescription = "Change the case of the selected text."

    parser = argparse.ArgumentParser(description=toolDescription)
    behaviors = parser.add_mutually_exclusive_group()
    behaviors.add_argument("--upper", action="store_true",
                           help="Change to uppercase.")
    behaviors.add_argument("--lower", action="store_true",
                           help="Change to lowercase.")
    behaviors.add_argument("--toggle", action="store_true",
                           help="Toggle the text case (default).")
    return parser.parse_args()


args = parseArguments()


if args.upper:
    processSelectedString(upperText)
elif args.lower:
    processSelectedString(lowerText)
else:
    processSelectedString(toggleText)
