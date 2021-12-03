'''
Geçen hafta neler gördük?
  1. for döngüsü, tekrarlı işlemler için kullanılıyor,
    while döngüsü ile aynı işi yapar ancak bazı fakları var:
      a) söz dizim, yazım farkı 
        ...
        while (şart):
          döngü gövdesi
          .....

        for iter in liste:
          döngü gözdesi

  2. fonksiyonlar (modüler programlama)
    y = f(x1,x2,x3,...) şeklinde düşünebiliriz.
      x1,x2,... : parametre
      y : geri gönüş değeri
      f : fonksiyon ismi (değişken tanımlama kurallarına uyulur)
    * bir fonksiyon kullanılmadan önce mutlaka tanımlanmalıdır.
    * def anahtar kelimesi ile tanımlanıyor.
'''
########################################################3
# Örnek uygulama 1 : Asal sayı

# bu fonksiyonun görevi kendisine parametre olarak gelen num değişkeninin asal olup olmadığını bulmak

'''
def isPrime(num): # num: parametre
  if num<2:   # 2 den küçükse asal değil
    return False
  elif num != int(num):  # ondalık sayı ise asal değil
    return False
  else:  # normal bir sayının testi
    divNum = 0
    for i in range(2,num-1):
      if (num%i == 0):
        divNum = divNum + 1
    if divNum == 0:
      return True
    else:
      return False


def allPrimes(n):
  lst = []
  for i in range(2,n):
    if isPrime(i):
      lst.append(i)
  return lst


n1 = 20
print(isPrime(n1)) # n1 değişkeni argüman dır

n2 = 100
lst2 = allPrimes(n2)
print(lst2)
'''
# mümkün olduğunca fonksiyonlara tek bir görev verin, bir fonksiyonda hem asal sayıların bulunması hem de ekrana yazılması doğru değil (single responsibility)

######################################################
# Örnek Uygulama 2: Bölenlerin bulunması ve mükemmel sayılar
'''
def divisorList(num):
  lst = []
  for i in range(1,num+1):
    if num%i == 0:
      lst.append(i)
  return lst

def isPerfect(num):
  lst = divisorList(num)
  if sum(lst[:-1]) == num:
    return True
  else:
    return False

def allPerfects(num):
  lst = []
  for i in range(1,num):
    if isPerfect(i):
      lst.append(i)
  return lst

n = 28
lst2 = divisorList(n)
print(lst2)

print(n,isPerfect(n))

n2 = 10000
lst3 = allPerfects(n2)
print(n2,"ye kadar olan mükemmel sayılar:",lst3)
'''
##################################################
# Örnek Uygulama 3:
'''
def adjacentElementsProduct(inputArray):
    max_ = inputArray[0]*inputArray[1]
    for i in range(1,len(inputArray)-1):
      pr = inputArray[i]*inputArray[i+1]
      if pr > max_:
        max_ = pr
    return max_

inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray)) # ekran: 21 olmalı, çünkü 7*3=21

def adjacentElementsProduct2(inputArray):
    lst = []
    for i in range(1,len(inputArray)-1):
      lst.append(inputArray[i]*inputArray[i+1])
    return lst
  
lst2 = adjacentElementsProduct2(inputArray)
print(lst2,max(lst2))
'''
####################################################
# Örnek Uygulama 4: shapeArea
'''
def shapeArea(n):
  return int((2*n-1)**2 - 4*(n-1)*n/2)

def shapeArea2(n):
  area = 0
  for i in range(1,n):
    area = area + 2*i-1
  return 2*n-1 + 2*area

n = 3
print(n,shapeArea2(n))
'''
###################################################3
# numpy, (ara dan sonra, 15dk)
'''
import lib4_15april as ml
n = 3
print(n,ml.shapeArea2(n))
print(ml.allPerfects(600))

import numpy as np
n1 = 5  # 0D arrar, skalar
        # 1D array, vector
        # 2D array, matrix
        # 3D+ array, tensor  arr[][][][][]
lst = [i for i in range(10)]
lst = [1,2,3,4,5]
print(lst)
lst.append("dnm")
print(lst)

'''
################################################################
import numpy as np

'''
arr = np.arange(10)
print(arr)

a = np.arange(0,15,dtype="int")
print(a)

b= a.reshape(3, 5)
print(b)
c = np.matrix(b)
print(c)

print("shape",b.shape) #Biçim
print(b.ndim) #Boyut sayısı
print(a.dtype.name) #Veri tipi
print(a.itemsize) #Arrayin her bir elemanının hafızada kapladığı alan, byte cinsinden
print(a.size) #Toplam eleman sayısı
print(type(a)) #Veri yapısı
'''
######################################################
'''
lst = [2,3,4]
a = np.array(lst)
print("*",a)
b = np.array([(1.5,2,3), (4,5,6)])
print("*",b)
c = np.array( [ [1+2j,2], [3,4] ], dtype=complex )
print("*",c)
print(c.dtype.name)
'''


'''
print(np.zeros( (3,4) ))
print(np.ones( (3,4,2) ))
print(np.ones(5))

print(np.empty((3,4)))

print(np.arange( 10, 30, 5 ))
print(np.linspace( 0, 2, 9 )) #0-2 aralığında doğrusal dağılımlı sayılar
'''
'''
arr = np.linspace(1,25,25)
print(arr)
arr = arr.reshape(5,5)
print(arr)
print(arr.flat[1])
arr2 = arr.copy(order='C')
print(arr2.flat[1])
'''

A = np.ones( (3,3) )
B = np.random.rand( 3,3 )
print(A,B,sep='\n')

C = A + B # basit aritmetik işlemler element düzeyinde yapılır
print(C)
