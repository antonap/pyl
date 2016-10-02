import random

guesses = 0
word = ''
secret_word = ''


def read_words(filename='20k.txt'):
    ''' Read file of most popular english words'''
    with open(filename) as words_file:
        words = words_file.read()
        words = [word for word in words.split('\n') if len(word) > 5]
    return words


def choose_random_word(words):
    ''' Choose random word from list '''
    return random.choice(words)


def show_word(word, guesses):
    print "Word:", word
    print "Guesses left:", guesses


def start_game():
    global guesses
    global word
    words = read_words('l2/20k.txt')
    word = str(choose_random_word(words))
    word = word.lower()
    guesses = len(word)


def read_char():
    while True:
        input_string = raw_input("Input char:")
        if (len(input_string)) == 0:
            continue
        user_char = input_string[0].lower()
        break
    return user_char


def run():
    global guesses
    show_word(word, guesses)
    hidden_word = list("*" * len(word))
    while(guesses > 0):
        print "Guess:", "".join(hidden_word)
        print "Try left:", guesses
        user_char = read_char()
        print "You char:", user_char
        if (user_char in word):
            print "Yes!"
            opened_char = [pos for pos, char in enumerate(word) if char == user_char]
            for pos in opened_char:
                hidden_word[pos] = word[pos]
        else:
            print "Oops! :("
        guesses = guesses - 1
        if "*" not in hidden_word:
            break
    if "*" not in hidden_word:
        print "You win this game!"
    else:
        print "Looser!"

start_game()
run()
