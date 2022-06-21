def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#-----------------------------------------------

def allPrimes(n):
    for i in range(2, n):
        if isPrime(i):
            yield i

################################################

def isPerfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

#-----------------------------------------------

def allPerfects(n):
    for i in range(1, n):
        if isPerfect(i):
            yield i

################################################

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

#-----------------------------------------------

def allPalindromes(n):
    for i in range(1, n):
        if isPalindrome(i):
            yield i

################################################

def fib(n):
  f0,f1,i = 0,1,1
  lst = [f0,f1]
  while(i<n):
    f0,f1,i = f1,f0+f1,i+1
    lst.append(f1)
  return lst
  
################################################