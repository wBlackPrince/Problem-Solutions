def f(start, end, count = 0):
   if start > end: return 0
   if start == end and count <= 2: return 1
   
   return f(start + 1, end, count) +  f(start*2, end, count+1) +  f(start*3, end, count+1)

print(f(1,100))
#1565