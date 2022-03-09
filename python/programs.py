import string

def freq(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def panagram(s):
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True

def biggest(l):
    if not l:
        return None
    m = l[0]
    for i in l:
        if i > m:
            m = i
    return m
        
