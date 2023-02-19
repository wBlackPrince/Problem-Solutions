def f(start, end, length = 0):
   if start == end and length <= 7: return 1
   if length > 7: return 0
   
   return f(start+1, end, length+1) + f(start*2, end, length+1) + f(start-3, end, length+1)

print(f(1,10))