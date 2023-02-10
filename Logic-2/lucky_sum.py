def lucky_sum(a, b, c):
  count=0
  list1=[a,b,c]
  for i in list1:
    if i==13:
      break
    count=count+i 
  return count  
