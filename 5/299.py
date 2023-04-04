def f(n):
   bini = bin(n)[2:]
   for i in range(2):
      if bini.count("1")%2 == 0:
         first = bini.find("1")
         bini = bini[first+1:]
      else:
         bini = "1" + bini + "00"
   return int(bini,2)

for i in range(2,100):
   if f(i) > 100:
      print(i)
      break