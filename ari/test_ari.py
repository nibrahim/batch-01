import ari

def test_nchars_0():
    assert ari.nchars("") == 0
    
def test_nchars_regular():
    assert ari.nchars("cat") == 3

def test_nchars_special():
    assert ari.nchars("black cat") == 8

def test_nchars_special2():
    assert ari.nchars("!@#$@#$$#%&^*&*&^") == 0
