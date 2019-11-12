def Hangaroo(secretWord):
    
    print('What is the secret word? Guess a letter!')
    print('You have 10 guesses.')
    print('The word has ' + str(len(secretWord)) + ' letters.')
    guess = ''
    lettersGuessed = []
    guessleft = 10

    while True: 
        
        guess = input()
        
        if guess in secretWord:
            if guess not in lettersGuessed:
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("You have "  + str(guessleft) + " guesses left!")
                
            elif guess in lettersGuessed:
                print("You already guessed that letter. Try again!")
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("You have "  + str(guessleft) + " guesses left!")
                
        elif guess not in secretWord:
            if guess in lettersGuessed:
                print("You already guessed that letter. Try again!")
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("You have "  + str(guessleft) + " guesses left!") 
            else:
                print("Oops! Wrong guess.")
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("You have "  + str(guessleft) + " guesses left!")
        
        if guessleft <= 0:
            print("You lost!")
            print("The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print("You won! Congratulations!")
            break
                
                
        
    
            
        