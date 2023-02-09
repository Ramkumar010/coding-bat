def sum13(nums):
  count=0
  i=0
  while i<len(nums):
    if nums[i]==13:
      i+=2
      continue
    count=count+nums[i]
    i+=1
  return count    
      
      
