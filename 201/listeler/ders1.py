#VERI YAPILARI

#listeler

#[]

#list()

notlar = [90, 80, 70, 50]

type(notlar)

liste = ["a", 19.3, 90]

liste_genis = ["a", 19.3, 90, notlar]

len(liste_genis)

liste_genis[0]
liste_genis[1]
liste_genis[3]

type(liste_genis[3])

tum_liste = [liste, liste_genis]

#del tum_liste


#Listeler - Eleman İşlemleri


liste = [10, 20, 30, 40, 50]

liste[0]
liste[1]
liste[6]

liste[0:2]

liste[:2]

liste[2:]

yeni_liste["a", 10, [20, 30, 40, 50]]
yeni_liste

yeni_liste[2]
yeni_liste[0:2]
yeni_liste[2][1]

#LİSTELER - Eleman Değiştirme

liste = ["ali", "veli", "berkcan", "ayse"]
liste

liste[1] = "velinin_babası"

liste

liste[1] = "veli"

liste[0:3] = "alinin_babası", "velinin_babası","berkcanın_babası"

liste = ["ali", "veli", "berkcan", "ayse"]
liste

liste = liste + ["kemal"]
liste

del liste[2]
liste

#listeler - Liste Metodları

liste = ["ali", "veli", "isik"]


dir(liste)

liste

#append

liste.append("berkcan")

liste

liste.remove("berkcan")

liste

#insert

liste = ["ali", "veli", "isik"]

liste
liste.insert(0, "ayse")

liste

liste= ["ali", "veli", "isik"]

liste[0] = "ayse"

liste
liste.insert(0,"ayse")

liste

liste[1] = "ali"

liste

liste.insert(2,"mehmet")
liste


liste.insert(5,"berk")
liste

len(liste)

liste.insert(len(liste), "beren")
liste

#pop

liste.pop(0)
liste

liste.pop(4)
liste

#count


liste = ["ali", "veli", "isik", "ali", "veli"]

liste.count("ali")
liste.count("veli")
liste.count("isik")

#copy()

liste_yedek = liste.copy()

#extend()


liste.extend(["a", "b", 10])
liste

#index()

liste.index("ali")

#reverse()

liste.reverse()
liste

#sort()

liste = [10, 40, 5, 90]
liste.sort()
liste


#clear

liste.clear()
liste
