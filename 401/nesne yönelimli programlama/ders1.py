# Nesne Yönelimli Programlama

# Sinif Nedir?


# Sinif Özellikleri (Class Attributes)

class VeriBilimci():
    bolum = ""
    sql = "Evet"
    deneyim_yili = 0
    bildigi_diller = []

# Siniflarin özelliklerine erişmek
VeriBilimci.bolum
VeriBilimci.sql

#Siniflarin özelliklerini değiştirmek
VeriBilimci.sql = "Hayır"
VeriBilimci.sql

# Sınıf Örneklendirmesi (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.sql

veli.bildigi_diller


# Ornek Ozellikleri

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""

    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)

ali.VeriBilimci()
ali.bildigi_diller
ali.bolum
veli.VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle("R")

ali.dil_ekle("R")
ali.bildigi_diller

veli.bildigi_diller("Python")

# Miras Yapıları

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
veribilimci1 = DataScience()
veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StroyTelling = ""

mar1 = Marketing()        


class Employees_yeni():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


ali = Employees_yeni("a", "b", "c")
ali.Address
