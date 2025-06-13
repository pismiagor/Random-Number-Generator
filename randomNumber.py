from time import *

def randomNumberGenerator(currentTime):
    number = str(currentTime).replace(".", "")
    j = 0
    randomNumber = []
    while j < len(number):
        randomNumber.append( j * int(number[j]))
        j += 1

    return int(str(sum(randomNumber))[-1])

def percengateCalculator(x: int):
    bits = [0 for _ in range(10)]
    for _ in range(x):
        bits[randomNumberGenerator(time())] += 1
    
    bits = [(i / x) * 100 for i in bits]
            
    print("Percentage of 0 is {} \nPercentage of 1 is {} \nPercentage of 2 is {} \nPercentage of 3 is {} \nPercentage of 4 is {} \nPercentage of 5 is {} \nPercentage of 6 is {} \nPercentage of 7 is {} \nPercentage of 8 is {} \nPercentage of 9 is {} \n".format(*bits) )
        
    return None
    

print(percengateCalculator(100))

print("Random number created is:",randomNumberGenerator(time()))
