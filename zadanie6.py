def seqProdUnl(* elementy):
     if(len(elementy) != 0):
         iloczyn = 1
         for x in range(len(elementy)):
             iloczyn*=elementy[x]
         return iloczyn
     else:
         return 0
print(seqProdUnl(1, 2, 3, 4, 5, 6))
