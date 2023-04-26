def f(x):
   d = "0123456789abcde"
   for i in d:
      a1 = int(i+"2c614",14)
      a2 = int("a8"+x+"6"+i+"0",14)
      if (a1+a2)%120 == 0:
         return x
   return False

for i in range(14):
   i1 = str(i)
   if f(i1):
      print((int("42c614",14) + int("a8"+i1+"640",14)) /120 )
      break