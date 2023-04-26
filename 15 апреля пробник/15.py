def f(a):
   for x in range(1,100):
      if not((x >= 8) <= ((x%3==0) or (x%2 == 0))  or (x+a >= 25)):
         return False
   return True

for a in range(1,200):
   if f(a):
      print(a)
      break