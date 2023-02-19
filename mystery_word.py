import random


def open_file(file):
    with open(file) as game_file:
        data = game_file.read()
        format_data = data.split()
        random_word = random.choice(format_data)
        random_word_list = list(random_word)
        blanks = [' _ '] * len(random_word)
    return random_word_list, blanks

print(open_file('words.txt'))

def choose_random_word(list):
    word = random.choice(list)
    return word

# def play_game():


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