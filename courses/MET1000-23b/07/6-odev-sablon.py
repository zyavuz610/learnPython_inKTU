lst = []
print("Gemideki odalardaki yük miktarlarını giriniz:")
print(" sonraki oda girişi için 0 değeri giriniz.")
print(" giriş tamamlandığında çıkmak için q giriniz.")
while(True):
  s = input("Yük miktarı? \> ")
  if (s == "q"):
    break
  else:
    lst.append(int(s))

print(lst)

############################################################
#     kodlarınızı bu alana yazınız

#############################################################