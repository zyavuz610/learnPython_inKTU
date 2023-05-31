"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, fonksiyon parametreleri, örnekler
  modüller, kendi modülümüzü yazmak
  datetime, math, 
  örnekler
  tuple veri yapısı, tuple üzerinde işlemler

Python - 126 : Uygulama: şehirler için plaka bulma örneği
"""

cities=("Türkiye","Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce")


while(1):
  in_ = input("Giriş => ")
  if in_ == 'q':
    break
  if in_ == '?' or in_ == 'help':
    print("Çıkmak için 'q'")
    print("Yardım için '?' veya 'help'")
    print("Plaka için 'p Trabzon'")
    print("Şehir için 'c 61'")
  arr = in_.split()
  if (arr[0] == 'p'):
    ind = cities.index(arr[1])
    if ind < 10:
      print(arr[1], "=>","0"+str(ind))
    else:
      print(arr[1], "=>",ind)
  if (arr[0] == 'c'):
    ind = int(arr[1])
    print(ind, "=>",cities[ind])
      

