"""
Seri: Örneklerle Python Programlama

Python 102 - Değişkenler ve Veri Türleri
- değişken nedir, değişkene değer atama (=)
- değişken isimlendirme
- değişkenlere çoklu değer atama
- değişkenleri ekrana yazma

- Veri Türleri

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

-----------------------------------------------

Değişkene İsim Verme Kuralları
1. büyük küçük harf ayrımı vardır, Sayi, sayi farklıdır
2. sadece alfabetik, sayısal karakterler kullanabiliriz
3. ek olarak _ kullanabiliriz.
4. en başa sayısal karakterler gelemez

Sayi, ok
sayi_1, ok
sayi1, ok
_sayi, ok
1sayi, hata
_, ok
"""
sayi1,sayi2 = 10, 25
toplam = sayi1 + sayi2
print("Birinci Sayı:",sayi1)
print("İkinci Sayı:",sayi2)
print("Toplam:",toplam)

isim = "Zafer"
print("Merhaba",isim)


# Veri Türleri

# Text Type:	str, (string) karakterlerden oluşan veri türüdür, tek tırnak veya çift tırnak kullanılarak ifade edilirler
soyad = "Yavuz"
sehir = 'Trabzon'


print(sehir)  # sehir, str
sehir = 61
print(sehir)  # sehir, int

# Numeric Types:	int, float, complex
sayi1 = -10 # int, tamsayı (integer)
s2 = 20.5 # float, kayan noktalı sayı
c2 = 2 + 3j
print(c2)

# Sequence Types:	list, tuple, range
# içerisinde birden çok veri barındıran yapılardır.

# Mapping Type:	dict, sözlük

# Set Types:	set, frozenset, küme


# Boolean Type:	bool, doğru yada yanlış değer olabilen veri
geldi_mi = True
print("Geldi mi?",geldi_mi)

# Binary Types:	bytes, bytearray, memoryview

# None Type:	NoneType