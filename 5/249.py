def f(n):
   bini = bin(n)[2:]
   for i in range(3):
      if bini.count("0") == bini.count("1"):
         bini += bini[-1]
      else:
         if bini.count("0") > bini.count("1"):
            bini += "1"
         else:
            bini += "0"
   return int(bini,2)


for i in range(91,10_000):
   g = f(i)
   if g%2 == 0 and g%4 != 0:
      print(i)
      break
#97