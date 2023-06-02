"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: string "", list [], tuple (), set {}, dict {}

Python 137 - Veri Yapılarını (list, dict) Kopyalamak | copy() Fonksiyonu | Copy-View Kavramı
Vscode kısayolları:
  Alt + Shift + ↓ : satır kopyala
  Alt + ↓ : satır taşı
  Ctrl + K + C : satırı yorum satırı yap
  Ctrl + K + U : yorum satırı yapmayı geri al

"""
s1 = "abc"
s1 = "abc"
s2 = s1 # deep copy
print(s1,s2)

s2 = "xyz"
print(s1,s2) # abc xyz

ls1 = ["a","b","c"]
ls2 = ls1 # soft copy
print(ls1,ls2,sep="==>")
ls2[0] = "x"
print(ls1,ls2,sep="==>")
ls2 = ls1.copy() # 1. yol, deep copy
ls2 = list(ls1) # 2. yol, deep copy
ls2 = ls1[:]   # 3. yol, deep copy
print(ls1,ls2,sep="\n")

print("-----------------------")
d1 = {
  "ad" : "Ali",
  "soyad" : "Yılmaz"
}
d2 = d1 # soft copy
d2 = d1.copy() # 1. yol, deep copy
d2 = dict(d1) # 2. yol, deep copy

print(d1,d2,sep="\n")
print("-----------------------")
d2 = d1
d2["soyad"] = "Yavuz"
print(d1,d2,sep="\n")
"""
"""