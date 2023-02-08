def same_first_last(nums):
  if len(nums)>=1:
    x=nums[-1]
    y=nums[0]
    if x==y:
      return True
  return False 
