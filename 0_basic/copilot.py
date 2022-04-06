def topla(a,b):
    return a+b

def asal_mi(sayi):
    for i in range(2,sayi):
        if sayi % i == 0:
            return False
    return True

def tum_asal_sayilar(n):
    for i in range(2,n):
        if asal_mi(i):
            print(i)

def obeb_al(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def maksimum(a,b):
    if a > b:
        return a
    else:
        return b

def topla(a,b):
    return a+b

def faktoriyel(n):
    sonuc = 1
    for i in range(2,n+1):
        sonuc *= i
    return sonuc

def mukemmel_mi(n):
    toplam = 0
    for i in range(1,n):
        if n % i == 0:
            toplam += i
    if toplam == n:
        return True
    else:
        return False
    
def isPerfectNumber(n):
    toplam = 0
    for i in range(1,n):
        if n % i == 0:
            toplam += i
    if toplam == n:
        return True
    else:
        return False

def isPerfect(n):
    toplam = 0
    for i in range(1,n):
        if n % i == 0:
            toplam += i
    if toplam == n:
        return True
    else:
        return False