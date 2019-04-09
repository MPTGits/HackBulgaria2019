import sys


def hangman(clue_word):
    print('Welcome to Hangman! Let the game begin!')
    list_clue_word=list(clue_word)
    user_guess_word=[' _ ' for char in list_clue_word]
    for tries in range(10):
        print(''.join(user_guess_word))
        letter=input('Guess a letter:')
        if letter in list_clue_word:
            for index in range(len(list_clue_word)):
                if list_clue_word[index]==letter:
                    user_guess_word[index]=letter
        print('Number of tries left:'+str(10-tries)+'\n')
        if ' _ ' not in user_guess_word:
            return 'You won!The word was '+''.join(user_guess_word)
    return '''You lost!
|    |    |
|  \ O /  |
|    |    |
|    |    |
|   / \   |'''

def main():
    word=sys.argv[1]
    print(hangman(word))

if __name__=='__main__':
    main()