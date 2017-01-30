def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all letters of secretWord are in lettersGuessed;
        False otherwise
    '''
    for letter in lettersGuessed:
        if letter in secretWord:
            secretWord = secretWord.replace(letter, '')
            if len(secretWord) == 0:
                return True
    return False
