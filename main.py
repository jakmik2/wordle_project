from statistics import mean
from wordle_sim import *


if __name__ == "__main__":
    wordle_agent = Agent()
    for i in range(3):
        wordle_sim(agent=wordle_agent)
    print(wordle_agent.guesses)
    print(f"{mean(wordle_agent.guesses)}")
