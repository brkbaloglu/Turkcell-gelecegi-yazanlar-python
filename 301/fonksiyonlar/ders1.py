print("a", "b", sep="_")

?print

print()

len("a")

4*4
4/4
5-1
6+3
3**2

#Fonksiyon nasıl yazılır?

4**2

def kare_al ():
    print(x**2)

kare_al(3)

def kare_al(x):
    print("Girilen sayının karesi:" + str(x**2))

kare_al(3)

def kare_al(x):
    print("Girilen sayı: " + str(x) + "Karesi: " str(x**2))

kare_al(3)
# Iki argümanlı fonksiyon tanimlamak

def kare_al(x):
    print(x**2)

def carpma_yap(x, y):
    print(x*y)

carpma_yap(2,3)

# On tanımlı argumanlar

?print

def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(3)


print("HELLO AI ERA")

#Argumanların Sıralaması

def carpma_yap(x, y=1):
    print(x*y)

carpma_yap(y = 2, x = 3)

carpma_yap(2,3)


# Ne zaman fonksiyon yazılır?

#ısı, nem, şarj


(40 + 25) / 90

def direkt_hesap(isi, nem, sarj):
    print((isi + nem) / sarj)

direkt_hesap(25, 40, 70)

# Çıktıyı Girdi Olarak Kullanmak

def direkt_hesap(isi, nem, sarj):
    print((isi + nem) / sarj)

cikti = direkt_hesap(25, 40, 70)
cikti
print(cikti)
direkt_hesap(25, 40, 70) * 9

def direkt_hesap(isi, nem, sarj):
    return (isi + nem) / sarj

cikti = direkt_hesap(25, 40, 70)
cikti
print(cikti)
direkt_hesap(25, 40, 70) * 9

def direkt_hesap(isi, nem, sarj):
    return (isi + nem) / sarj


direkt_hesap(25, 40, 70)

# Local ve Global Değişkenler

x = 10
y = 20

def carpma_yap(x = 2, y = 1):
    return x*yazılır

carpma_yap(2,3)

# Local Etki Alanından Global Etki Alanını Değiştirmek

x = []
#del x

def eleman_ekle(y):
    x.append(y)
    print(str(y) + "ifadesi eklendi")

eleman_ekle("ali")

eleman_ekle("veli")
x