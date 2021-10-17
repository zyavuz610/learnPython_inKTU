'''
Bu derste;
  - Python hakkında genel bilgi
  - program yazmak nedir? (veri+işlem yapmak)
  - print() fonksiyonu
  - değişkenler, veri tipleri
  - aritmetik operatörler
  - if, elif, else (koşul operatörleri)
'''

#####################################################
# python kodları uzantısı .py olan dosyalara yazılır.

# yorum satırı # ile başlar.

# program yazmak demek, veri + işlem (fonksiyon)
'''
print("Merhaba Dünya")    # print() fonksiyon
print("Merhaba", "Zafer")
print("Merhaba", "Zafer","Yavuz",sep='--')
'''
####################################################
# değişkenler = veri saklama nesneleri (bellek bölgeleri)
'''
a = 5
b = 10
c = a+b
print("Toplam",c)
'''
###################################
# değişken isimlendirme kuralları
#   [a-z][A-Z][0-9]_ kullanılabilir
#   rakam en başa gelemez
#   büyük küçük harf ayrımı vardır.
'''
midterm_grade = 50
final_grade   = 45

# avg_grade = (midterm_grade + final_grade) / 2
avg_grade = 0.5*midterm_grade + 0.5*final_grade

print(midterm_grade,final_grade,"=",avg_grade)
'''
######################################################
#   başka işlemler var mı
#   +,-,*,/    %, //, **     ---> aritmetik operatörler
'''
a0 = 10
n = 2
a1 = a0 ** n
print("üs alma",a1)

n2 = 75
divisor = n2 % 7
print("kalan",divisor)

n3 = 475
d = n3 // 10
print("sonuç",d)
'''

#######################################################
'''
#   dört işlem      : +, -, *, /
#   tam sayı bölme  : //      --> bir yılın kaçıncı yy'a ait alduğunu bulun ?
#   mod             : %
#   üs al, çoğalt   : **
A = 2+2
A = 22/7    # türü default olarak <float>
print("A",type(A))
B=2 * (3 + 4)               #parantez içerisindeki ifadenin işlem önceliği vardır.
print("B") 

# Float sayı tipi:
# Tam sayı (integer) olmayan sayıların sunulmasında kullanılan tip. (Integer: 4, float: 4.00) Python bir integer ve bir float sayıyı, integer sayıyı arka planda floata çevirmek suretiyle birlikte işleme tabi tutabilir.
# Üs alma işlemi:
c = 2**5
d = 9**0.5
print(c,d,type(d))

# Zincir şeklinde de üs alma işlemi yapılabilir:
f = (9**0.5)**4

# Bölme işleminde Bölüm ve Kalan:
k = 20 // 6

l = 1.25 % 0.5

print(A,B,c,d,f,k,l)
'''
#######################################################
'''
# operatör öncelikleri
# *, /, %, // operatörleri +, - ye göre daha önceliklidir.

a = 2*4 + 7
b = 7 + 4*2
c = 2 * (4+7)     # parantez, en öncelikli operatördür
print("a:",a,"b:",b,"c:",c)
'''
#######################################################
'''
year = 1701
century = (year-1)//100 + 1

print("sonuç",century) # 18

'''

'''
if year % 100 == 0:
  century = year//100
else:
  century = year//100 + 1
print("sonuç",century) # 18
'''

##########################################################
# program = veri + işlem (bilgi + saymak)
# veri türleri

'''
Temel Veri Türleri
1. tamsayılar, int
2. reel sayılar, float
3. boolean, bool
4. karakter, char

'''

year = 2003
year = int(input("Year: "))
is_leap_yaer = (year%400 == 0) or (year%4==0 and year%100 != 0)
print("sonuç",is_leap_yaer)

# bir yıl, eğer 4 e bölünüyorsa, 100'e bölünmüyorsa, 400'e bölünüyorsa artık yıldı

##################################################
