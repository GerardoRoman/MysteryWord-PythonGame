import random


def open_file(file):
    with open(file) as game_file:
        data = game_file.read()
        format_data = data.split()
        random_word = random.choice(format_data)
        random_word_list = list(random_word)
        blanks = [' _ '] * len(random_word)
    return random_word_list, blanks
# print(open_file('words.txt'))


def play_game():
    word, underscores = open_file('words.txt')
    print(f''' Welcome to Mystery Word Game!
        The secret word has {len(word)} letters.
        Your current guess: {' '.join(underscores)}''')
    wrong_guesses = []
    guesses_remaining = 8
    while guesses_remaining > 0:
        guess_made = input("Guess a letter! ").lower()
        print('guess_made: ', guess_made)
        if guess_made in wrong_guesses:
            print('Try again!')
            guesses_remaining += 0 
        elif guess_made in underscores:
            print('You already guessed that. Try again!')
            guesses_remaining += 0
        elif guess_made in word:
            guesses_remaining -= 1
            for i in range(len(word)):
                if guess_made == word[i]:
                    underscores[i] = guess_made
        else:
            wrong_guesses.append(guess_made)
            guesses_remaining -= 1
        print('Answer: ', ' '.join(underscores))
        print('Wrong guesses: ', wrong_guesses)
        print('Guesses remaining: ', guesses_remaining)
        if underscores == word:
            print('You win! The word is: ', ' '.join(word))
            break
        if guesses_remaining == 0:
            print('Out of guesses! The word was ', ' '.join(word))
            break
        

















# EXAMPLE FROM CLASS::
# def play_game():
#     word = 'apple'
#     wrong_guesses = ['b', 'd']
#     right_guesses = []
    
#     game_board = ''
#     for letter in word:
#         game_board += ' '
#         if letter in right_guesses:
#             game_board += letter + ' '
#         else:
#             game_board += "_ "
#     print(game_board)


# do not change code below this line
if __name__ == "__main__":
    play_game()