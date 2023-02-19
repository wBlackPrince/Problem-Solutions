

def f(start, count = 0):
   
   if count == 11 and start < 0 : 
      return [start]
   if count > 11: return []
   
   return f(start - 2, count+1) +  f(start*(-3), count+1)

print(len(set(f(97))))
#656