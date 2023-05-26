"""
Seri: Örneklerle Python Programlama ve Algoritma

Python 100 - Python ile programlamaya giriş
Python 101 - Python ile Ekrana Çıktı Yazmak, print() fonksiyonu
Python 102 - Değişkenler ve Veri Türleri

Python 103 - Aritmetik operatörler ve not ortalaması bulma örneği

+, -, *, /
aritmetik operatör,
sağ tarafındaki değeri alır, sol tarafındaki değeri alır, işlem yapar ve tek bir değer oluşturur.

3 tane daha aritmetik, %, //, **
- mod alma, bölümünden kalan bulma, %
- üs alma, **
- tam sayı bölme, //

Atama operatörü, =
+=
-=
*=
/=
%=
//=
**=
"""

ders = "Matematik" # str
not1 = 55 # int, %25
not2 = 76 # %25
not3 = 86 # %50

toplam = not1 + not2 + not3
#         55  +  70
#        125 + not3 = 211
# toplam = 211


#ort = 0.25*not1 + 0.25*not2 + 0.5*not3 # float

ort = 1 + toplam // 3 # tamsayı bölümü
print(ders,"dersinin ortalaması:",ort)

rakam = ort%10 # mod alma
print(ort,"sayısının birler basamağındaki rakam:",rakam)

not4 = (toplam%10) ** 2
print("Not 4:",not4)

not4 = not4 + 10 # 10 ekleme, 10 artırma
not4 += 10 # 10 ekleme,
not4 -= 5 # 5 azaltma
not4 *= 2 # 2 katını alma
