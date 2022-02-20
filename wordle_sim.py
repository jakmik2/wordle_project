from random import sample
from agent import *


def get_hints(wordle: str, wordle_map: dict, guess: str) -> str:
    d = wordle_map.copy()
    out_string = ""
    for i, char in enumerate(guess):
        # check if this char is the same as wordle
        if char == wordle[i]:
            out_string += char
            d[char] -= 1
        # Check if char is in the word, but not this position
        elif char in d.keys() and d[char] != 0:
            d[char] -= 1
            out_string += "+"
        else:
            out_string += "-"
    # print(out_string)
    return out_string


def wordle_sim(**kwargs) -> bool:
    """ Simulate Game of Wordle
    (1) Pick a random word from the word bank to be the "wordle"
    (2) receive user guesses -> return information regarding guess
    (3) resolve victory or loss after 6 guesses
    """
    defaultKwargs = {'agent': None}
    kwargs = defaultKwargs | kwargs

    # Get valid answers
    with open("wordle-answers-alphabetical.txt", 'r') as f:
        content = f.read()
    valid_answers = content.split("\n")
    # Get valid guesses
    with open("wordle-allowed-guesses.txt", 'r') as f:
        content = f.read()
    valid_guesses = content.split("\n")
    wordle = sample(valid_answers, 1)[0]
    wordle_map = {}
    for char in wordle:
        wordle_map[char] = wordle_map.get(char, 0) + 1
    training = False
    if kwargs['agent'] is not None:
        training = True
        agent = kwargs['agent']
        agent.reset()


    # Get User
    if not training:
        print("Thank you for playing!\nEnter first guess below!\n")

    guessing = True
    counter = 0
    # print(wordle) # debugging
    victory = False
    while guessing:
        if training:
            guess = agent.guess()
        else:
            guess = input().lower()
        if guess not in valid_answers and guess not in valid_guesses:
            if not training:
                print("Not a Valid entry")
        else:
            # print(guess)
            counter += 1
            if guess == wordle:
                victory = True
                if training:
                    pass
                else:
                    print("You Win!")
                guessing = False
            if guess != wordle:
                # Return string of hints
                hint = get_hints(wordle, wordle_map, guess)
                print(hint)
                if training:
                    agent.interpret_hint(guess, hint)
        if counter == 6 and training is False:
            guessing = False

    if training:
        agent.guesses.append(counter)
        print(wordle)
    elif victory:
        print(f"Good job, it took you {counter} to guess {wordle}")
    else:
        print(f"So close! You failed to guess {wordle}")
    return victory
