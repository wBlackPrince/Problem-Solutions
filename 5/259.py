def f(n):
   bini = bin(n)[2:]
   if "0" not in bini: return False
   zero = bini.rfind("0")
   bini = bini[:zero] + bini[:2] + bini[zero+1:]
   return int(bini[::-1],2)

print(f(58))

#58