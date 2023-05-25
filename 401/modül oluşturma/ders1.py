#Modul oluşturmak

#HesapModulu.py

def yeni_maas(x):
    print(x * 20/100 + x)

maaslar = [1000, 2000, 3000, 4000]

#test

import HesapModulu
HesapModulu.yeni_maas(1000)

import HesapModulu as hm
hm.yeni_maas(2000)

#hatalar / istisnalar (exceptions)

a = 10
b = 0

a/b

try: 
    print(a/b)
except ZeroDivisionError:
    print("Paydada sifir olamaz")

# tip hatasi
a = 10
b = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Sayi ve string problemi")