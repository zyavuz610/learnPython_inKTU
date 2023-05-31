# kullanıcıdan 1. sayıyı al
sayi1 = input("1. sayıyı giriniz:")
sayi1 = int(sayi1)
print("Girilen sayı:",sayi1,",Türü:",type(sayi1))

# kullanıcıdan 2. sayıyı al
sayi2 = input("2. sayıyı giriniz:")
sayi2 = int(sayi2)
print("Girilen sayı:",sayi2,",Türü:",type(sayi2))

# kullanıcıdan işlem al
islem = input("İşlem giriniz (+,-,/,*):")
print("Girilen işlem:",islem,",Türü:",type(islem))

# işlem yap
if (islem == "+"):
  sonuc = sayi1 + sayi2

if (islem == "-"):
  sonuc = sayi1 - sayi2

if (islem == "*"):
  sonuc = sayi1 * sayi2

if (islem == "/"):
  sonuc = sayi1 / sayi2

# sonucu ekrana yaz
print("Sonuç:",sonuc)