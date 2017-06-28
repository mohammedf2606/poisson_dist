import math  # For e and factorial
import random  # Generate random stuff
import matplotlib.pyplot as plt  # Graphing

probList = []

mean = int(input("Enter the mean: "))
trials = int(input("How many numbers do you want? "))

pProb = lambda x: math.e**(-mean) * (mean**x)/math.factorial(x)

def CumulativeCompare():
    rand = random.random()
    currentProb = 0
    currentCumu = 0
    while True:
        currentCumu += pProb(currentProb)
        if currentCumu <= rand:
            currentProb += 1
        else:
            return currentProb

def Simulate():
    poList = []
    for i in range(trials + 1):
        poList.append(CumulativeCompare())
    return poList

if __name__ == '__main__':
    poList = Simulate()
    poss = [x for x in range(max(poList) + 1)]
    for i in poss:
        count = 0
        count = poList.count(i)
        probList.append(count)
    plt.plot(poss,probList)
    plt.show()
