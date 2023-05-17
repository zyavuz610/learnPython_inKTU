def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def printAllPrimes(n):
    for i in range(2, n):
        if isPrime(i):
            print(i,end=',')
    print("")

printAllPrimes(100)

def sumArray(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = iter(range(1, 10))
next(arr)

for i in arr:
    print(i,end=",")