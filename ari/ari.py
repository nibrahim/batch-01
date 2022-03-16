"""
Utilities to calculate automated readability index as per forumula in https://en.wikipedia.org/wiki/Automated_readability_index

Copyright 2021 - Noufal Ibrahim <noufal@hamon.in>
"""

import math

def nchars(s):
    count = 0
    for i in s:
        if i.isalnum():
            count += 1
    return count


def nwords(s):
    return s.count(" ")

def nsentences(s):
    return s.count(".") + s.count("!") + s.count("?")

def index(chars, words, sentences):
    c = 4.71 * (chars/words)  + 0.5 * (words/sentences) - 21.43
    return math.ceil(c)

def ari(paragraph):
    idx = index(nchars(paragraph), 
                nwords(paragraph),
                nsentences(paragraph))

    vals = {1: ("5-6","Kindergarten"),
            2: ("6-7","First Grade"),
            3: ("7-8","Second Grade"),
            4: ("8-9","Third Grade"),
            5: ("9-10","Fourth Grade"),
            6: ("10-11","Fifth Grade"),
            7: ("11-12","Sixth Grade"),
            8: ("12-13","Seventh Grade"),
            9: ("13-14","Eighth Grade"),
            10: ("14-15","Ninth Grade"),
            11: ("15-16","Tenth Grade"),
            12: ("16-17","Eleventh Grade"),
            13: ("17-18","Twelfth Grade"),
            14: ("18-22","College student ")}

    return vals[idx]
