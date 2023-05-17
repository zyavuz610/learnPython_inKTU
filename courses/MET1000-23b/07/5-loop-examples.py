"""
Örnek:
 öğrenci adı ve 2 adet not al
 ortlama > 50 olanlar geçebilsin,
 tüm öğrencilerin geçti/kaldı durumlarnı ekrana yaz
 öğrenci sayısı belli değil, çıkış için q ya basılsın
"""

print("[Ad not1 not2] şeklinde giriş yapınız.")
print("çıkış için q")
while (True):
    s = input("Giriş:\> ")
    print("Giriş:",s)
    if(s == "q"):
        break
    kisi = s.split() # kisi bir liste oldu
    #print(kisi)
    n1 = int(kisi[1])
    n2 = int(kisi[2])
    ort = (n1+n2)/2
    if(ort > 50):
        print(kisi[0],"geçti")
    else:
        print(kisi[0],"kaldı")

