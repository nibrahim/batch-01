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

def test_nsenteces_periods():
    assert ari.nsentences("I am here. I am sitting.") == 2

def test_nsentences_exclamation():
    assert ari.nsentences("I am here! I am shouting!") == 2

def test_nsentences_question():
    assert ari.nsentences("I am here. Where are you?") == 2

def test_nsenteces_multiple():
    assert ari.nsentences("I've been here for a long time! Where are you? Why are you not coming here? I've been asking for you.") == 4

