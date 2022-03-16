import random

ALREADY_GUESSED = 0
CORRECT = 1
WRONG = 2

def get_word(wordfile="/usr/share/dict/words"):
    good_words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >=5:
                good_words.append(i)
    return random.choice(good_words)


def mask_word(secret_word, guesses):
    op = []
    for i in secret_word:
        if i in guesses:
            op.append(i)
        else:
            op.append("-")
    return "".join(op)

def get_status(secret_word, guesses, turns_remaining):
    masked_word = mask_word(secret_word, guesses)
    guessed_letters = " ".join(guesses)
    return f"""Secret word:{masked_word}
Guesses : {guessed_letters}
Remaining turns : {turns_remaining}"""

def check(secret_word, guesses, turns_remaining, new_guess):
    if new_guess in guesses:
        return ALREADY_GUESSED, turns_remaining
    else:
        guesses.append(new_guess)
        if new_guess in secret_word:
            return CORRECT, turns_remaining
        else:
            return WRONG, turns_remaining-1

        
def game_over(secret_word, guesses, turns_remaining):
    if turns_remaining == 0:
        return True, f"You lost! The word was {secret_word}"
    masked = mask_word(secret_word, guesses)
    if "-" in masked:
        return False, None
    else:
        return True, f"You guessed it! The word was {secret_word}"
    
    
def main():
    secret_word = get_word()
    print (secret_word)
    guesses = []
    turns_remaining = 8
    while True:
        print (get_status(secret_word, guesses, turns_remaining))
        guess = input("Enter a letter ")
        
        status, turns_remaining = check(secret_word, guesses, turns_remaining, guess)
        if status == ALREADY_GUESSED:
            print ("You already guessed that")
        
        finished, message = game_over(secret_word, guesses, turns_remaining)
        if message:
            print (message)
        if finished:
            break


if __name__ == "__main__":
    main()
            
            
        
