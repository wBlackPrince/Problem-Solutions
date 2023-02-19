def f(start, end):
   if start > end: return 0
   if start ==end: return 1
   
   n = len(bin(start)[2:])
   return f(start+1, end) +  f(start + 2**n, end)

print(f(4,49))
# 33