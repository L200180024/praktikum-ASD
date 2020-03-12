#NAMA : Muhammad Mahatma Rosyid Habibilah
#NIM  : L200180024

##No.1
def cetakSiku(x):
   for k in range(1, x+1):
       print (k*'*')

##No.2
def gambarlahPersegiEmpat(c,d):
   for i in range(c):
      if i == 0 or i == c-1:
         print('@'*d)
      else:
         print('@'+' '*(d-2)+'@')

##No.3a
def jumlahHurufVokal(x):
   vokal = 'aiueo'
   jumlah = 0
   for i in x:
      if i.lower() in vokal:
         jumlah += 1
   return (len(x), jumlah)
print(jumlahHurufVokal('Surakarta'))

##No.3b
def jumlahHurufKonsonan(a):
   vokal = 'aiueo'
   jumlah = 0
   for i in a:
      if i.lower()not in vokal:
         jumlah += 1
   return (len(a), jumlah)
print(jumlahHurufKonsonan('Surakarta'))

##No.4
def rerata(c):
   jumlah = 0
   for i in c:
      jumlah += i
   return jumlah/len(c)

##No.5
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n >= 0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2, int(sq(n))+1):
            if (n % 2) == 1:
                if (data % 3) != 0:
                    if (data % 5) != 0:
                        return True
                else:
                    return False

##No.6
data = [2,3,5]
for k in range (2, 1000):
   if k in data:
      print(k)
   elif (k%2) == 1:
      if (k%3) != 0:
         if (k%5) != 0:
            print(k)
            
##No.7
def faktorPrima(l):
   list = [ ]
   loop = 2
   while loop <= l:
      if (l % loop) == 0:
         l /= loop
         list.append(loop)
      else:
         loop += 1
   return list
print(list)

##No.8
def apakahTerkandung(h,k):
    return h.lower() in k.lower()
   
##No.9
for a in range (1, 100):
    if (a % 3) == 0 and (a % 5) == 0:
        a = "Python UMS"
    elif (a % 3) == 0:
        a = "Python"
    elif (a % 5) == 0:
        a = "UMS"
    print(a)

##No.10
from math import sqrt as akar
def selesaikanABC (a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if (D < 0):
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b + akar(D))/(2*a)
        hasil = (x1, x2)
        return hasil

      
##No.11
def apakahKabisat(tahun):
   kabisat = False
   if (tahun % 400 == 0):
      kabisat = True
   elif tahun % 100 == 0:
      kabisat = False
   elif tahun % 4 == 0:
      kabisat = True
   print('Itu tahun kabisat') if kabisat else print('Itu bukan tahun kabisat')

##No.12
import random
rdm = random.randint(1, 100)
print("""Permainan tebak angka.\nSaya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.""")
m = "Masukkan tebakan ke-"
o = ":> "
c = 1
d = str(c)
for i in range (1, 100):
    e = (m + d + o)
    a = int(input(e))
    c += 1
    d = str(c)
    if (a < rdm):
        print("Itu terlalu kecil. Coba lagi.")
    elif (a > rdm):
        print("Itu terlalu besar. Coba lagi.")
    elif (a == rdm):
        print("Ya. Anda benar")
        break

##No.13
angka = {1:"satu " , 2:"dua " , 3:"tiga " , 4:"empat " , 5:"lima " , 6:"enam " , 7:"tujuh " , 8:"delapan " , 9:"sembilan "}
b = "puluh "
c = "ratus "
d = "ribu "
e = "juta "
f = "milyar "
g = "triliun"

def katakan(k):
    y = str(k)
    n = len(y)
    if n <= 3:
        if n == 1:
            if y == "0":
                return ""
            else:
                return angka[int(y)]
        elif n == 2:
            if y[0] == "1":
                if y[1] == "1":
                    return "sebelas"
                elif y[0] == "0":
                    k = y[1]
                    return katakan(k)
                elif y[1] == "0":
                    return "sepuluh"
                else:
                    return angka[int(y[1])]+ "belas"
            elif y[0] == "0":
                k = y[1]
                return katakan(k)
            else:
                k = y[1]
                return angka[int(y[0])]+ b + katakan(k)
        else:
            if y[0] == "1":
                k = y[1:]
                return "seratus "+ katakan(k)
            elif y[0] == "0":
                k = y[1:]
                return katakan(k)
            else:
                k = y[1:]
                return angka[int(y[0])]+ c + katakan(k)
    elif 3 < n <= 6:
        p = y[-3:]
        q = y[:-3]
        if q == "1":
            return "seribu " + katakan(p)
        elif q == "000":
            return katakan(p)
        else:
            return katakan(q) + d + katakan(p)
    elif 6 < n <= 9:
        r = y[-6:]
        s = y[:-6]
        return katakan(s) + e + katakan(r)
    elif 9 < n <=12:
        t = y[-9:]
        u = y[:-9]
        return katakan(u) + f + katakan(t)
    else:
        v = y[-12:]
        w = y[:-12]
        return katakan(w) + g + katakan(v)

##No.14
def formatRupiah(s):
    a = str(s)
    if len(a) <= 3:
        return "Rp " + a
    else:
        y = a[-3:]
        z = a[:-3]
        return formatRupiah(z) + "." + y
        print ("Rp " + formatRupiah(z) + "." + y)
