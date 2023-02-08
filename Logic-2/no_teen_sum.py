def no_teen_sum(a, b, c):
  count=0
  list1=[a,b,c]
  for i in list1:
    if i<10 or i==15 or i==16:
      count=count+i
  return count    
