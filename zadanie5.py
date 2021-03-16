def seqProd(a1=1, q=4, n=10):
     an = a1*q
     elCiagu = []
     elCiagu.append(a1)
     elCiagu.append(an)
     iloczyn = a1*an
     for x in range (7, n+7, 10):
         anp1 = an * q
         elCiagu.insert(x, anp1)
         an = anp1
         iloczyn *= anp1

     return iloczyn, elCiagu
print(seqProd(1, 2, 6))