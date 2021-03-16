produkty = {"baton":"szt", "cola":"puszka", "banan":"kg","orzechy laskowe":"kg"}
print(produkty)

prodSzt = [produkt for produkt in produkty.keys() if produkty[produkt] =="szt"]
print(prodSzt)