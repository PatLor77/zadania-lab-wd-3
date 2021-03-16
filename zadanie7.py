def shopping(**koszyk):
     items = len(koszyk)
     if items != 0:
         suma = 0
         ceny = [cena for cena in koszyk.values() if isinstance(cena, float) == True or isinstance(cena, int) == True]
         print(ceny)
         for x in range (len(ceny)):
             suma+=float(ceny[x])

     else:
         return "Brak zakupów"
     return suma

print(shopping(cola = 5, paczek = 3, redbull = 7, cosciekawego = 17))

