def f(start, end):
   if start == 21 or start > end: return 0
   if start == end: return 1
   
   n = start + 1 if start%2 != 0 else start+2
   return f(start + 1, end) +  f(start+4, end) +  f(start + n, end)

print(f(2,11)*f(11,26))
#493