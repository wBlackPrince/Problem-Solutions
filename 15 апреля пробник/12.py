def f(a):
   i = len(a)
   b = ""
   while i>0:
      c = a[i-1]
      b += str(c)
      i -= 3
   return b

print(f("2"*10 + "4"*10))