def trapField(a=1, b=1, h=1):
    if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(h).isdigit() == False):
         return "Podano bledne wartosci"
    else:
         a = float(a)
         b = float(b)
         h = float(h)
         if (a<=0)|(b<=0)|(h<=0):
             return "Podano bledne wartosci"
         else:
             P = (a+b)*h/2
             return P

print(trapField())
