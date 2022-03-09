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

def test_biggest_positive():
    ret = biggest([1,2,3,4])
    assert ret == 4

def test_biggest_negative():
    ret = biggest([-1,-2,-3,-4])
    assert ret == -1
