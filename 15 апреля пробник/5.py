def f(n):
   bini = bin(n)[2:]
   for i in range(2):
      bini = bini + ("0" if bini.count("1") == 2 else "1")
   return int(bini,2)

c=0
for i in range(1,1000):
   if 64 <= f(i) <= 72:
      c+=1
print(c)