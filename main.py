import random

def main():
    win = 0
    lose = 0
    for _ in range(100000):
        correct = random.randint(0,4)
        selection = random.randint(0,4)
        eliminate = random.randint(0,4)
        while eliminate == correct or eliminate == selection:
            eliminate = random.randint(0,4)
        eliminate2 = random.randint(0,4)
        while eliminate2 == correct or eliminate2 == selection or eliminate2 == eliminate:
            eliminate2 = random.randint(0,4)
        eliminate3 = random.randint(0,4)
        while eliminate3 == correct or eliminate3 == selection or eliminate3 == eliminate or eliminate3 == eliminate2:
            eliminate3 = random.randint(0,4)
        old_select = selection
        while selection == old_select or selection == eliminate or selection == eliminate2 or selection == eliminate3:
            selection = random.randint(0,4)
        
        if selection == correct:
            win += 1
        else:
            lose += 1
    print(f"Win: {win}\nLose: {lose}")

if __name__ == "__main__":
    main()