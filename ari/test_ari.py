import ari

def test_nchars_0():
    assert ari.nchars("") == 0
    
def test_nchars_regular():
    assert ari.nchars("cat") == 3

def test_nchars_special():
    assert ari.nchars("black cat") == 8

def test_nchars_special2():
    assert ari.nchars("!@#$@#$$#%&^*&*&^") == 0

def test_nwords():
    "words is the number of spaces"
    assert ari.nwords(" ") == 1

def test_nwords_multiple():
    assert ari.nwords("words is the number of spaces") == 5
    
# Sentences is the sum of the number of . ? ! 
def test_nsentences_none():
    assert ari.nsentences("I am here") == 0
