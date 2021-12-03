import zylib

print(zylib.isPrime(4))

for i in zylib.allPrimes(100):
    print(i,end=" ")


print("\n",zylib.isPerfect(28))
arr = zylib.allPerfects(10000)
for i in arr:
    print(i,end=" ")


print("\n",zylib.isPalindrome(28))

for i in zylib.allPalindromes(10000):
    print(i,end=" ")