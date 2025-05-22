from random import choice, randint
import numpy as np


def MontyHallSimulation(doors):
    if doors < 2:
        print("Sorry that is invalid")
        raise ValueError
    correct = randint(0,doors - 1)
    selection = randint(0, doors - 1)
    chosen = [correct, selection]
    eliminations = []
    for _ in range(doors - 2):
        eliminated = choice([i for i in range(0, doors) if i not in chosen and i not in eliminations])
        eliminations.append(eliminated)
    selection = choice([i for i in range(0, doors) if i not in eliminations and i != selection])
    if selection == correct:
        return True
    return False

def main():
    win = 0
    lose = 0
    doors = int(input("How many doors would you like to have in the game show: "))
    while doors < 2:
        doors = int(input("That is an invalid number of doors. there needs to be at least 2 so you can switch at the end: "))
    simulations = int(input("How many simpulations would you like to do: "))
    while simulations < 1:
        simulations = int(input("You need to try at least one simulation, Enter the number of simulations again: "))
    for _ in range(simulations):
        simu = MontyHallSimulation(doors)
        if simu:
            win += 1
        else:
            lose += 1
    print(f"Win: {win}\nLose: {lose}")

if __name__ == "__main__":
    main()
