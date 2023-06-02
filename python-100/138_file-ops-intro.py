"""
Dosya İşlemleri
  Ubuntu basit dosya listeleme
  dosya aç
  dosya oku, ekrana yaz

Açıklama:
  Bilgisayarda her şey dosya olarak saklanır, kaynak kodlar da dosya olarak saklanır.
  Veriler üzerinde işlem yapmak için bu verileri dosyalarda saklarız.
  dosyalar 3 türlüdür:
    1. veri dosyaları: metin, resim, video, ses, ...
    2. program dosyaları: çalıştırılabilir dosyalar, exe, word, notepad, ...
    3. sistem dosyaları: işletim sistemi dosyaları, dll, sys, ...
  dosyaların adı ve uzantısı vardır.
    UZANTI: dosyanın türünü belirtir.
    dosya adı: dosyanın ismidir.
    metin.txt.exe -> metin.txt dosyasıdır, exe uzantılıdır.
    autoexec.bat -> autoexec dosyasıdır, bat uzantılıdır.
  veri dosyaları ile uğraşacağız.
    txt, csv, json, xml, ...

  Python Dosya İşlemleri
    1. dosya açma
    2. dosya okuma, yazma, işlemleri
    3. dosya kapatma

"""
opened_file = open('file.txt')  # dosya açma
readString = opened_file.read()        # dosyayı oku
opened_file.close()             # dosyayı kapat
newList = readString.split("\n") # satırlara ayır
print(readString)
print(newList)
print(len(readString),len(newList))