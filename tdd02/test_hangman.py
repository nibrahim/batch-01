import os

import hangman


def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_mask_word_single_letter():
    secret_word = "elephant"
    guesses = ["l"]
    ret =hangman.mask_word(secret_word, guesses)
    assert ret == "-l------"

def test_mask_word_single_letter():
    secret_word = "elephant"
    guesses = ["e"]
    ret =hangman.mask_word(secret_word, guesses)
    assert ret == "e-e-----"

def test_mask_word_none():
    secret_word = "elephant"
    guesses = ["x"]
    ret =hangman.mask_word(secret_word, guesses)
    assert ret == "--------"

def test_mask_word_complete():
    secret_word = "elephant"
    guesses = ["e", "l", "p", "h", "a", "n", "t", "x", "q"]
    ret =hangman.mask_word(secret_word, guesses)
    assert ret == "elephant"

def test_mask_word_noguesses():
    secret_word = "elephant"
    guesses = []
    ret =hangman.mask_word(secret_word, guesses)
    assert ret == "--------"
    
def test_get_status_basic():
    secret_word = "helicopter"
    guesses = ["c", "o", "x"]
    turns_remaining = 3
    ret = hangman.get_status(secret_word, guesses, turns_remaining)
    assert ret == """Secret word:----co----
Guesses : c o x
Remaining turns : 3"""

def test_get_status_no_guesses():
    secret_word = "helicopter"
    guesses = []
    turns_remaining = 8
    ret = hangman.get_status(secret_word, guesses, turns_remaining)
    assert ret == """Secret word:----------
Guesses : 
Remaining turns : 8"""

def test_check_already_guessed():
    secret_word = "hospital"
    guesses = ["i", "t"]
    turns_remaining = 5
    new_guess = "t"
    status, turns_remaining = hangman.check(secret_word, guesses, 
                                            turns_remaining, 
                                            new_guess)
    assert status == hangman.ALREADY_GUESSED
    assert turns_remaining == 5
    assert guesses == ["i", "t"]
    
    
def test_check_correct():
    secret_word = "hospital"
    guesses = ["i", "t"]
    turns_remaining = 6
    new_guess = "p"
    status, turns_remaining = hangman.check(secret_word, guesses, 
                                            turns_remaining, 
                                            new_guess)
    assert status == hangman.CORRECT
    assert turns_remaining == 6
    assert guesses == ["i", "t", "p"]

    
def test_check_wrong():
    secret_word = "hospital"
    guesses = ["i", "t", "p"]
    turns_remaining = 6
    new_guess = "x"
    status, turns_remaining = hangman.check(secret_word, guesses, 
                                            turns_remaining, 
                                            new_guess)
    assert status == hangman.WRONG
    assert turns_remaining == 5
    assert guesses == ["i", "t", "p", "x"]

    
def test_game_over_not_over():
    secret_word = "policeman"
    guesses = ["x", "t"]
    turns_remaining = 5
    finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
    assert not finished
    assert message == None

def test_game_over_over_won():
    secret_word = "rabbit"
    guesses = ["r", "a", "b", "i", "t"]
    turns_remaining = 5
    finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
    assert finished
    assert message == "You guessed it! The word was rabbit"


def test_game_over_over_lost():
    secret_word = "rabbit"
    guesses = ["r", "a", "b", "i", "t"]
    turns_remaining = 0
    finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
    assert finished
    assert message == "You lost! The word was rabbit"

    
    
    
