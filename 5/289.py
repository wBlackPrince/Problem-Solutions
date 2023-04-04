def f(n):
   bini = bin(n)[2:]
   if bini.count("1")%2 == 0:
      bini = "1"+bini+"00"
   else:
      bini = "11" + bini
   return int(bini,2)

for i in range(2,1000):
   if f(i) >= 412:
      print(i)
      break