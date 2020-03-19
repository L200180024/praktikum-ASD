#Nama : M.Mahatma Rosyid Habibilah
#Nim  : L200180024

#no 1
e = [[8,2],[3,5]]
f = [[5,1],[3,8]]
g = [[22,1,"x","y"],[7,13,9]]
h = [[1,9],[8,5],[6,4]]
i = [[7,2,4],[8,6,3],[6,7,3]]

def CekKonsisten(a):
    d = len(a[0])
    c = 0
    for i in range(len(a)):
        if (len(a[i]) == x):
            c+=1
    if(c == len(a)):
        print("matriks konsisten")
    else:
        print("matriks tidak konsisten")

CekKonsisten(e)
CekKonsisten(f)
CekKonsisten(g)

def CekAngka(a):
    r = 0
    u = 0
    for i in a:
        for j in i:
            u+=1
            if (str(j).isdigit()== False):
                print("tidak semua isi matriks adalah angka")
                break
        else:
            r+=1
    if(r==u):
        print("semua isi matriks adalah angka")

CekAngka(e)
CekAngka(f)
CekAngka(g)

def Ordo(a):
    x,y = 0,0
    for i in range(len(a)):
        x+=1
        y = len(n[i])
    print("mempunya ordo"+str(x)+"x"+str(y))

Ordo(e)
Ordo(f)
Ordo(g)
Ordo(h)

def JumlahMatriks(a,b):
    x,y = 0,0
    for i in range(len(a)):
        x+=1
        y = len(a[i])
    xy = [[0 for j in range(x)] for i in range(y)]

    z = 0
    if(len(a) == len(b)):
        if(len(a[i])) == len(b[i]):
            z=+1
    if(z==len(a) and z==len(b)):
        print("matriks sama")
        for i in range(len(a[i])):
            xy[i][j] = a[i][j] + b[i][j]
        print(xy)
    else:
        print("matriks berbeda ordo")

JumlahMatriks(e,f)
JumlahMatriks(b,h)

def Perkalian(a,b):
    p = 0
    x,y = 0,0
    for i in range(len(a)):
        x+=1
        y = len(a[i])
    h,o = 0,0
    for i in range(len(b)):
        h+=1
        o = len(b[i])
    if(y==h):
        print("dapat di kalikan")
        kk = [[0 for j in range(o)] for i in range(x)]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    kk[i][j] += a[i][k] * b[k][j]
        print(kk)
    else:
        print("tidak dapat di kalikan")

data = [[4,7,2],[1,9,3]]
data1 = [[5],[4],[1]]
Perkalian(data,data1)
Perkalian(e,f)
Perkalian(g,e)
Perkalian(data,h)

def Determinan(T, total=0):
    x =len(T[0])
    y = 0
    for i in range(len(T)):
        if(len(T[i]) == x):
            y+=1
    if(y == len(T)):
        if(x==len(T)):
            indices = list(range(len(T)))
            if len(T) == 2 and len(T[0]) == 2:
                hsl = T[0][0] * T[1][1] - T[1][0] * T[0][1]
                return hsl
            for gg in indices:
                DF = T
                DF = DF[1:]
                height = len(DF)
                for i in range(height):
                    DF[i] = DF[i][0:DF] + DF[i][DF+1:]
                hehe = (-1) ** (DF % 2)
                sub_det = Determinan(DF)
                total += hehe * T[0][DF] * sub_det
        else:
            return "tidak dapat mengitung determinan, bukan matriks bujursangkar"
    else :
        return "tidak dapat menghitung determinan, bukan matriks bujursangkar"
    return total

bb = [[5,1],[8,-3]]
yy = [[6,9,1],[7,5,2],[2,-1,2]]
zz = [[0,-4,2],[7,4,9],[-4,0,0],[3,-2,1]]
print(Determinan(bb))
print(Determinan(yy))
print(Determinan(zz))
print(Determinan(f))
print(Determinan(g))
      
#no 2
def Nol(a,b=None):
    if(b==None):
        b=a
    print("membuat matriks 0 dengan ordo"+str(a)+"x"+str(b))
    print([[0 for j in range(b)]for i in range(a)])

Nol(4,8)
Nol(5)

def Identitas(a):
    print("membuat matriks dentitas dengan ordo"+str(a)+"x"+str(b))
    print([[1 if j==i else 0 for j in range(a)] for i in range(a)])

Identitas(3)
Identitas(2)

#no 3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def tambahDepan(self, data_baru):
        node_baru = Node(data_baru)
        node_baru.next = self.head
        self.head = node_baru
    def tambahAkhir(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def Menyisipkan(self, data, posisi):
        node = Node(data)
        if not self.head:
            self.head = node
        elif posisi == 0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_posisi = 0
            while(current_posisi < posisi) and current.next:
               prev = current
               current = current.next
               current_posisi +=1
            prev.next = node
            node.next = current
        return self.head
    def Delete(self, posisi):
        if self.head == None:
            return
        temp = self.head
        if posisi == 0:
            self.head == temp.next
            temp = None
            return
    for i in range(posisi -1):
        temp = temp.next
        if temp is None:
            break
        if temp.next is None:
            return
            next = temp.next.next
            temp.next = None
            temp.next = next
    def menampilkan(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    def mencari(self, v):
        current = self.head
        while current != None:
            if current.data == v:
                return "True"
            current = current.next
        return "False"

coba = LinkedList()
coba.tambahDepan(32)
coba.tambahDepan(33)
coba.tambahDepan(34)
coba.tambahAkhir(35)
coba.Delete(2)
coba.Menyisipkan(1,5)
print(coba.mencari(32))
print(coba.mencari(40))
coba.menampilkan()

#no 4
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
class DoublyLinkedList:
    def __int__(self):
        self.head = None
    def awal(self, data_baru):
        print("menambah data di awal", data_baru)
        node_baru = Node(data_baru)
        node_baru.next = self.head
        if self.head != None:
            self.head.prev = node_baru
        self.head = node_baru
    def akhir(self, data_baru):
        print("menambah data di akhir", data_baru)
        node_baru = Node(data_baru)
        node_baru.next = None
        if self.head is None:
            node_baru.prev = None
            self.head = node_baru
            return
        last = self.head
        while(last.next != None):
            las = last.next
        last.next = node_baru
        node_baru.prev = last
        return
    def tampil(self , node):
        print("\n Dari depan:")
        while(node != None):
            print(" % d" %(last.data))
            last = last.prev

coba = DoublyLinkedList()
coba.awal(10)
coba.awal(4)
coba.akhir(7)
coba.akhir(5)
coba.tampil(coba.head)
