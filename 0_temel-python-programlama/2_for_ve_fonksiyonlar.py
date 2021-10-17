########################################################
'''
Bir önceki derste
  birden çok veri barındıran veri yapılarını gördük
  1. string, katar, karakter dizisi (kelime, cümle) 
    - oluşturma, str = "deneme"
        s = 'ali veli' 
    - indisleme, dilimleme
        s[0], s[s:5], s[start,stop,step], s[-1]
    - string fonksiyonları (*,+,replace())
      s="ali"
      s = s+s  "ali"
  2. liste (list)
    - oluşturma, [...]
    - indisleme, dilimleme
    - ekleme, silme
  3. döngüler while
    - while döngüsü
      1) başlangıç, Start 
      2) bitiş şartı, Stop
      3) artış, step, 
      4) döngü gövdesi
'''
#######################################################
#   Geçtiğimiz Haftaki Ödevler 
#######################################################
# covid-19 vaka analizi
'''
covid_case = [1,0,1,0,4,12,29,51,93,
              168,311,277,289,293,343,
              561,1196,2069,1704,1815,
              1610,2704,2148]
print(covid_case,len(covid_case))
sum_of_case = sum(covid_case)
print("Toplam Vaka Sayısı:",sum_of_case)
sum_of_first10 = sum(covid_case[0:10])
print(covid_case[0:10],"İlk 10 gündeki vaka sayısı:",sum_of_first10)

inc_rate = []
i = 1
while i<len(covid_case):
  dif = covid_case[i] - covid_case[i-1]
  inc_rate.append(dif)
  #print(dif)
  i = i + 1

max_rate = max(inc_rate)
day_of_max_rate = inc_rate.index(max_rate)
print(inc_rate,max_rate,day_of_max_rate+1)
# print("En fazla artış olduğu gün:",max_rate)

cs_dailysum_array = []
# range(start,stop,step)
for i in range(len(covid_case)):
  daily_sum = sum(covid_case[0:i+1])
  cs_dailysum_array.append(daily_sum)

print("Günlük Sayılar:",cs_dailysum_array)
'''
################################################
'''
s = 0
for i in range(1,101,2):
  s = s + i
print(s)

s = 0
for i in range(82):
  s = s+i
print(s)

s = sum(range(82))
print(s)
'''

################################################
'''
0. K = 0
1. H = 1
2. HK = 1
3. HHK = 2
4. HHHKK = 3
5. HHHHHKKK = 5
8, 13, 21, 34, 55, 89, ....
....
'''
##########################################################
'''
infected = 0
incubation = 1

lst = [infected]
day = 1
while day<=28:
  #####################       
  incubation,infected = infected, incubation + infected
  lst.append(infected)
  day = day + 1
print(lst,lst[-1])
'''
#####################################################
'''
# yer değiştirme
midExam = 65
finExam = 78

#temp = midExam;midExam = finExam;finExam = temp
midExam, finExam = finExam, midExam

print(midExam,finExam)
'''

###########################################################
'''
covid_case = [1,0,1,0,4,12,29,50,93,
              168,311,277,289,293,343,
              561,1196,2069,1704,1815,
              1610,2704,2148]
arr = [1,2,1,5,4,12,9,8,11,10]
arr = covid_case
for i in range(len(arr)):
  str = "*"
  if(arr[i] !=0):
    line = str * (1+arr[i]//50)
    print(line,"-",arr[i])
  else:
    print(" ","-",arr[i])
'''
######################################################
# farklı liste oluşturma biçimleri
#A = {X | xEN ve x <5}
# A = {0,1,2,3,4}
'''
A = [x for x in range(5)]
B = [2*x for x in range(51)]
C = [x for x in range(101) if x%2==0]
D = [i for i in range(82)]
print(sum(D))
'''
#####################################################
# moduler programlama, kullanıcı tanımlı fonksiyonlar 

# y = f(x1,x2,x3,...)
# f: x1,x2,..... -> y
'''
def mySum(a,b):
  s = a+b
  return s

print(mySum(3,5))
print(mySum(13,15))
'''
######################################################
'''
n = 10

fact = 1
for i in range(n):
  fact = fact * (i+1)
print(fact)

n = 15
fact = 1
for i in range(n):
  fact = fact * (i+1)
print(fact)

n = 7
fact = 1
for i in range(n):
  fact = fact * (i+1)
print(fact)
######################################################
def myFact(n):
  fact = 1
  for i in range(n):
    fact = fact * (i+1)
  return fact

print(myFact(10))
print(myFact(15))
print(myFact(7))
'''
###########################################################
'''
import sys
print(sys.version)

import math
print(math.floor(7.8))

print(math.factorial(10))
print(math.gcd(120,80))

print(math.sin(math.pi / 6) + math.cos(0))
print(math.pi)
print(math.e)
print(math.radians(180))
'''
#########################################################
import numpy
import matplotlib
arr = numpy.asarray([1,3,5,7,9])
print(arr)
matplotlib.plot(arr)
