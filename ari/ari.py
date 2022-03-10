"""
Utilities to calculate automated readability index as per forumula in https://en.wikipedia.org/wiki/Automated_readability_index

Copyright 2021 - Noufal Ibrahim <noufal@hamon.in>
"""

def nchars(s):
    count = 0
    for i in s:
        if i.isalnum():
            count += 1
    return count


def nwords(s):
    count = 0
    for i in s:
        if i == " ":
            count += 1
    return count
