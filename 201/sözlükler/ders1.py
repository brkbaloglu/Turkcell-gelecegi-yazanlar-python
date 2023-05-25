#Veri Yapıları - Dictionary (Sözlük)

#Sozluk Oluşturma
sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk

len(sozluk)

sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}

sozluk

sozluk = {"REG" : ["RMSE", 10],
          "LOJ" : ["MSE", 20],
          "CART" : ["SSE", 30]}

sozluk

# Sozluk Eleman İslemleri

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk[0]
sozluk["REG"]
sozluk["LOJ"]


sozluk = {"REG" : ["RMSE", 10],
          "LOJ" : ["MSE", 20],
          "CART" : ["SSE", 30]}

sozluk["REG"]

sozluk = {"REG" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          "LOJ" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          "CART" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30}}

sozluk
sozluk["REG"]["SSE"]

# Sozluk - Eleman Ekleme & Değiştirme


sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Çoklu Doğrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Ağları"

sozluk
l = [1]
l

sozluk[l] = "yeni bir şey"
t = ("tuple", )
sozluk[t] = "yeni bir şey"
sozluk