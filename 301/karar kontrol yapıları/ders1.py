# Karar Kontrol Yapıları

# True False Sorgulamaları

sinir = 5000

sinir == 4000


sinir == 5000


5 == 4

5 == 5


#if 

sinir = 50000
gelir = 60000

gelir < sinir

if gelir < sinir:
    print("Gelir sinirdan kucuk")
if gelir > sinir:
    print("Gelir sinirdan buyuk")


#else 
sinir = 50000
gelir = 35000

if gelir > sinir:
    print("Gelir sinirdan buyuk")
else:
    print("Gelir sinirdan kucuk")

#diger ornek
sinir = 50000
gelir = 50000

if gelir == sinir:
    print("Gelir sinira esittir")
else:
    print("Gelir sinira esit degildir")


#elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print("Tebrikler, hediye kazandınız")
elif gelir1 < sinir:
    print("Uyarı!")
else:
    print("Takibe devam")

if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız")
elif gelir2 < sinir:
    print("Uyarı!")
else:
    print("Takibe devam")

# mini uygulama

sinir = 50000
magaza_adi = input("Magaza adi nedir")
gelir = int(input("Gelirinizi giriniz:"))

if gelir > sinir:
    print("Tebrikler," + magaza_adi + "promosyon kazandınız")
elif gelir < sinir:
    print("Uyarı! Çok düşük gelir" + str(gelir) )
else:
    print("Takibe devam")
