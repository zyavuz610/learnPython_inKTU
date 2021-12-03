'''
Bir önceki ders neler gördük?
  1. program nedir = veri + işlem yapmak

veri bölümünde
  - değişken tanımlama kuralları
  - veri türleri  
    * int, float, boolean, str, char ...
  
işlem yapmak bölümünde
  - print(...,...,...) fonksiyonu
  - operatörler
    * aritmetik: girdisi sayı, sonuç sayı
      +,-,*,/ : 4 işlem
      % : mod alma
      // : tamsayı bölümünde
      ** : üs alma
    * diğer
      = : atama, a = 5,         5 = a,   a=b, a=5, a="merhaba"
      , : birbirine eş ifadeleri ayırmak için
    * karşılaştırma, girdi sayı, çıktı doğru ya da yanlış
      == : eşit ise (a == b)
      != : eşit değil ise (a!=b)
      <, <=, >, >= : küçük, büyük karşılaştırma
    * ilişkisel
      and, or, not      a<b or b>c,     a<6 and a>3
      karşılaştırma sonuçlarını birleştirmek için
  - if, elif, else (koşul ifadeleri)

Örnek olarak
  * artık yıl ve öğrencilerin notları problemini yeniden çözelim.
  * harf not bulucu
  * bankamatik problemi

'''

#############################################
# aşağıdaki kodda soru işareti yerine duğru kodu yazınız

'''
year = 1203

leap_year = False
if year%4 == 0 :
  leap_year = True
if year%100 == 0 : 
  leap_year = False
if year%400 == 0 :
  leap_year = True
# leap_year = (year%400 == 0) or (year%4 == 0 and year%100 != 0)
print("sonuç",leap_year)
'''
'''

a = True
b = False

res = (not a) and (not b) #   (a or b)'
print(res)
'''
# (a and b)' = a' or b'
# (a or b)' = a' and b'

# not(a and b) = (not a) or (not b)



########################################################
'''
first_coeff = 0.4   # arasınav katsayısı
final_coeff = 0.6   # final katsayısı

first_grade = 78    # arasınav notu
final_grade = 65    # final notu


# aşağıdaki kodu tamamlayınız

avg_grade = first_coeff*first_grade + final_coeff*final_grade # code here


# 0-45    FF    45-53   CC    53-61   CB
# 61-69   BB    69-77   BA    77-100  AA

if avg_grade < 45 :
  grade_word = "FF"
elif avg_grade < 53:    
  grade_word = "CC"
elif avg_grade < 61:
  grade_word = "CB"
elif avg_grade < 69:
  grade_word = "BB"
elif avg_grade < 77: 
  grade_word = "BA"
else : 
  grade_word = "AA"
print("avg(",first_grade,final_grade,") =",avg_grade,"(",grade_word,")",sep='\n')
'''

########################################################
'''
money_amount = 1355
_200 = money_amount // 200
remaining = money_amount % 200
_100 = remaining // 100
remaining = money_amount % 100
_50 = remaining // 50
remaining = money_amount % 50
_20 = remaining // 20
remaining = money_amount % 20
_10 = remaining // 10
remaining = money_amount % 10
_5 = remaining // 5
remaining = money_amount % 5

print("Verilen para miktarları:")
print("200 =",_200)
print("100 =",_100)
print("50 =",_50)
print("20 =",_20)
print("10 =",_10)
print("5 =",_5)
'''

########################################################
'''
Bu derste
  birden çok veri barındıran veri yapılarına bakacağız
  1. string, katar, karakter dizisi (kelime, cümle) 
    - indisleme, dilimleme
    - örnek: stringin tersini bulalım
  2. liste (list)
    - oluşturma, (range(start,stop,step)), b = [x for x in range(100)]
    - indisleme, dilimleme
    - ekleme, silme
  3. döngüler, for, while (zaman kalırsa)
    - for i in range(start,stop,step)
    - x = [x for x in range(10) if (....)]
    - örnek: For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21. 7 and 3 produce the largest product.
    - ekrana n boyutlu (üçgen, baklava dilimi, içi boş baklava dilimi) çizelim. alanlarını bulalım.
    - corona dağılım grafiğini çizelim (yatay grafik)
'''
#######################################################
'''
#    01234567
s = "Merhaba KTÜ, Python programlamayı sevdiniz mi?"  # karakter dizisi
# veriler üzerinde ne yapılabilir? 1) oluşturma, 2)erişme(okuma), 3) değiştirme
print(s)    # diziye topluca erişim

print(s[1:5])
print(s[1:7:2]) # [start:stop:step]

print(s[-5:-1],s[-1])

s2 = "ey edip adanada pide yermisin"
print(s2)
print(s2[3:10:2])
print(s2[::-1])
'''
###########################################################
# Listeler
# veriler üzerinde ne yapılabilir? 1) oluşturma, 2)erişme(okuma), 3) değiştirme
'''
list1 = [1,2,3,4,5,6]
print(list1)
print(list1[0:5:2])
print(list1[::-1])

covid19TR = [1,1,2,5,18,47,96,187,311,385,1186]
covid19TR[3] = 6
covid19TR[-2] = 685

print(covid19TR)

print("son 3 gün:",covid19TR[-3::1])   # son 3 gün

num = len(covid19TR)
print(num)
'''
###################################################################
'''
covid19TR = [1,1,2,5,18,47,96,187,311,385,1186,1525,1818,2433,3629,5698,7402,9217,10827,13531]

del(covid19TR[-1])
num = len(covid19TR)
print("Toplam Adet:",num)
Sum = sum(covid19TR)
print("Toplam Miktar:",Sum)

today = [500, 600, 700]
# covid19TR.extend(today)
covid19TR = covid19TR + today


print(covid19TR)
num = len(covid19TR)
print("Toplam Adet:",num)
Sum = sum(covid19TR)
print("Toplam Miktar:",Sum)

covid19TR.append("ktu")
print(covid19TR)

q = 384 in covid19TR
print(q)

i = covid19TR.index(600)
print(i)
'''
#############################################################
# Döngüler = Loop 
# Tekrarlı kodları çalıştırmak için kullanılır.
# for, while gibi döngü yapıları var,
#    4 parçadan oluşur, 1) döngünün başlangıcı, 2) döngünün bitişi (şartı) 3) adım, 4) döngünün gövdesi

counter = 1
Sum = 0
while counter<=1000:
  if (counter%3 == 0 or counter%5 == 0) :
    Sum = Sum + counter
    #print(counter,Sum)
  counter = counter + 1

print(counter,Sum)

'''
counter = 0
True, döngü gövdesi çalışın
  ekrana yaz, 0, 
  counter = 1
while - True
  ekrana yaz, 1
  counter = 2
while - True
  ekrana yaz, 2
  counter = 3
while - True
  ekrana yaz, 3
  counter = 4
while - False
while dan çıktı, devam etti
'''
