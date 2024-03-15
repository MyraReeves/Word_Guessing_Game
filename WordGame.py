import time
PlayerName = input('Hello! Welcome to my word guessing game!  What is your name?   ')
print ('')
print ('The objective of this game is to try to guess a chosen word in 11 guesses or less')
print ('Good luck, ' + PlayerName + '!')

print('')


def start():
    print(' ')
    print('I have thought of a word')
    SecretWord = 'ostrich'
    Guesses = ''
    RemainingTurns = 11
    while RemainingTurns > 0:
        Wrong_Answers = 0
        for Letter in SecretWord:
            if Letter in Guesses:
                print(Letter)
            else:
                print('__')
                Wrong_Answers += 1
        if Wrong_Answers == 0:
            print('')
            print('Congratulations ' + PlayerName +'! 🎉 YOU WON!!!! 🎉')
            print('You correctly guessed the secret word: ' + SecretWord)
            print('')
            break
        print('')
        Guess = input('Guess a letter that might be in the word:   ').lower()
        Guesses += Guess

        if Guess not in SecretWord:
            RemainingTurns -= 1
            print('')
            print('Sorry. That letter is not in the word.')
            print('You have ' + str(RemainingTurns) + ' more guess left.')
            print('Please try again')
            if RemainingTurns == 0:
                print('I\'m sorry, ' + PlayerName + ', but you have run out of available guesses. ☹ You lost.')
                print('The word was: ' + SecretWord )
                print('GAME OVER. Better luck next time!')
                time.sleep(1)
    def Restart():
        print('')
        NewGame = input('Yes or no, would you like to play again?  ').lower()
        print('')
        if NewGame == 'no':
            print('Thank you for having played!  Good-bye, ' + PlayerName +'!')
            time.sleep(1.75)
            quit()
        if NewGame == 'yes':
            print('Wonderful!  I will come up with a new word for you to guess!')
            time.sleep(2)
            start()
        else:
            print('')
            print('Invalid response. Please answer with either "yes" or no"')
            Restart()
    Restart()

start()

