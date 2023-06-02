def isPrime(n):
    if n <= 1:
        return False
    i=2
    while i*i <= n:
        if n % i == 0: # bölümden kalan sıfır ise
            return False
    return True

sonuc = isPrime(359334085968622831041960188598043661065388726959079837)
print(sonuc)

def allPrimes(n):
    lst = []
    for i in range(2,n):
        if isPrime(i):
            lst.append(i)
    return lst

lst = allPrimes(100)
print(lst)