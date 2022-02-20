"""
Docstring about agent class
"""
from random import sample
import string

ALPHABET = [char for char in string.ascii_lowercase]


class Agent:
    def __init__(self):
        self.incorrect_letters = []
        self.correct_letters = {} # KEY char VALUE list of incorrect positions
        self.guess_list = [None] * 5
        self.words_tried = []
        self.guesses = []

    def guess(self) -> str:
        # Use heuristics of letters_used and correct_letters to make a guess
        while True:
            correct_letters_temp = self.correct_letters.copy()
            guess_string = ""
            for i in range(5):
                if self.guess_list[i] is not None:
                    guess_string += self.guess_list[i]
                elif correct_letters_temp:
                    picking_letter = True
                    tracker = 0
                    while picking_letter:
                        random_letter = sample(correct_letters_temp.keys(), 1)[0]
                        list_in_question = correct_letters_temp[random_letter]
                        if i not in correct_letters_temp[random_letter]:
                            del correct_letters_temp[random_letter]
                            break
                        tracker += 1
                        if tracker >= len(correct_letters_temp.keys()):
                            random_letter = sample(ALPHABET, 1)[0]
                            break
                    guess_string += random_letter
                else:
                    random_letter = sample(ALPHABET, 1)[0]
                    guess_string += random_letter
            if guess_string not in self.words_tried:
                self.words_tried.append(guess_string)
                break
        return guess_string

    def interpret_hint(self, guess: str, hint: str) -> None:
        # "-" is incorrect
        # "+" is correct but in the wrong position
        # any char indicates right letter in right position
        for i, char in enumerate(hint):
            if char in ALPHABET:
                self.guess_list[i] = char
                if char in self.correct_letters.keys():
                    del self.correct_letters[char]
            elif char == "+":
                self.correct_letters[guess[i]] = self.correct_letters.get(guess[i], [])
                if not self.correct_letters[guess[i]]:
                    self.correct_letters[guess[i]].append(i)
                elif i not in self.correct_letters[guess[i]]:
                    self.correct_letters[guess[i]].append(i)
            else:
                if guess[i] not in self.incorrect_letters:
                    self.incorrect_letters.append(guess[i])
        return

    def results(self):
        print(self.correct_letters)
        print(self.incorrect_letters)
        print(self.guess_list)

    def reset(self):
        self.incorrect_letters = []
        self.correct_letters = {}  # KEY char VALUE list of incorrect positions
        self.guess_list = [None] * 5
        self.words_tried = []


