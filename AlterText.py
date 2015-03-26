#!/usr/bin/python
# -*- coding: latin-1 -*-

from ProcessSelection import setClipboardData, sendPasteKey, \
                             processSelectedString
import argparse


def hyphenateText(text):
    setClipboardData(text.replace(" ", "-"))
    sendPasteKey()


def hashtagText(text):
    import re
    textAlphaOnly = re.sub(r'\W+', '', text)
    hashtag = "#" + textAlphaOnly.lower()
    setClipboardData(hashtag)
    sendPasteKey()


def urlShortener(text):
    from urllib2 import Request, urlopen, URLError

    request = Request('http://is.gd/api.php?longurl=' + text.strip())

    try:
        response = urlopen(request)
        shortURL = response.read()
        setClipboardData(shortURL)
        sendPasteKey()
    except URLError:
        pass


def parseArguments():
    toolDescription = "A few functionalities for altering "\
                      "the selected text."

    parser = argparse.ArgumentParser(description=toolDescription)
    behaviors = parser.add_mutually_exclusive_group()
    behaviors.add_argument("--hyphenate", action="store_true",
                           help="Replace spaces with hyphens.")
    behaviors.add_argument("--hashtag", action="store_true",
                           help="Convert the string to a hashtag, #likethis.")
    behaviors.add_argument("--shortenURL", action="store_true",
                           help="Convert the string to a short URL via is.gd.")
    return parser.parse_args()


args = parseArguments()


if args.hyphenate:
    processSelectedString(hyphenateText)
elif args.hashtag:
    processSelectedString(hashtagText)
elif args.shortenURL:
    processSelectedString(urlShortener)
