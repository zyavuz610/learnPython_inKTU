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