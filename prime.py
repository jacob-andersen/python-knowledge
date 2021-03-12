# small python function to check if a given number is a prime number

def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if(numberToCheck%x == 0):
            return False
        return True