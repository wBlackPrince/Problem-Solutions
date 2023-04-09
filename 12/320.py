mini = (100,0)
for n in range(1,100):
   for x in range(1,100):
      for y in range(1,100):
         for z in range(1,100):
            t =  66+n-3*x - 2*y -4*z
            if t < mini[0] and mini[0]>=0:
               mini = (t,n)
               print(mini)
#1
