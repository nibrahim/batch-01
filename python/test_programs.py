from programs import freq, panagram, biggest

def test_same():
    ret = freq("aaa")
    assert ret == {"a" : 3}

def test_multiple():
    ret = freq("aaabbcccc")
    assert ret == {"a": 3, "b" : 2, "c": 4}

def test_panagram_true():
    assert panagram("the quick brown fox jumps over the lazy dog")

def test_panagram_false():
    assert not panagram("the quick brown fox jumped over the lazy dog")


def test_biggest_empty():
    ret = biggest([])
    assert ret == None

