#nama = Muhammad Mahatma Rosyid Habibilah
#nim = L200180024

#no 1a
class Pesan(object):
    """Sebuah class bernama Pesan.
       Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else :
            return False

#no 1b
    def hitungKonsonan(self):         
        k = self.teks
        vokal = 'aiueoAIUEO'
        jum = 0
        for i in k :
            if i.lower() not in vokal:
                jum += 1
        return jum
    
#no 1c
    def hitungVokal(self):
        vocal = 0
        z = self.teks
        huruf = "aiueoAIUEO"
        for i in z:
            if i in huruf:
                vocal += 1
        return vocal
    
#no 2a
class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class manusia.
           Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal
#no 2b
    def perbaruiKotaTinggal(self, berubah):
        self.kotaTinggal = berubah
#no 2c
    def tambahUangSaku(self, plus):
        self.uangSaku += plus

#no 3
#print("Masukkan Data Mahasiswa Di bawah Ini :")
#a = input("Nama Mahasiswa      : ")
#b = input("NIM Mahasiswa       : ")
#c = input("Asal Mahasiswa      : ")
#d = input("Uang Saku Mahasiswa : ")
#mhs = Mahasiswa(a, b, c, d)

#no 4    
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)

#no 5
    def hapusKuliah(self, hapus):
        self.listKuliah.remove(hapus)

#no 6
class SiswaSMA(Manusia):
    """Class Siswa merupakan turunan dari class Manusia"""
    def __init__(self, nama, NISN, jur, alamat):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.nisn = NISN
        self.jurusan = jur
        self.alamat = alamat
    def __str__(self):
        a = 'Nama       : ' + str(self.nama) \
            +'NISN      : ' + str(self.nisn) \
            +'Alamat    : ' + str(self.alamat) \
            +'Jurusan   : ' + str(self.jurusan)
        print (a)
    
    def ambilNama(self):
        print (self.nama)
    def ambilNisn(self):
        print (self.nisn)
    def ambilJurusan(self):
        print (self.jurusan)
    def ambilAlamat(self):
        print (self.alamat)
        
#no 7
class MhsTIF(Mahasiswa):   
    """Class MhsTIF merupakan turunan dari class Mahasiswa"""
    def katakanPy(self):
        print('Python amaze')



# Metode atau state yang muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
# Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, sehingga MhsTIF mewarisi semua properties dari Mahasiswa maupun Manusia.

#Dari class Manusia:
#    1. nama
#    2. keadaan
#    3. ucapkanSalam
#    4. makan
#    5. olahraga
#    6. mengalikanDenganDua

#Dari class Mahasiswa:
#    1. NIM
#    2. kotaTinggal
#    3. uangsaku
#    4. ambilNama
#    5. ambilNIM
#    6. ambilUangSaku
#    7. makan
#    8. ambilKotaTinggal
#    9. perbaruiKotaTinggal
#    10. tambahUangSaku
#    11. listKuliah
#    12. ambilKuliah
#    13. hapusKuliah

#Dari class MhsTIF:
#    1. katakanPy


        
    
    
    
        
        
