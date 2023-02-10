def array_front9(nums):
  count=len(nums)
  if len(nums) >=4:
    count=4
  for i in range (count):
      if nums[i]==9:
        return True
  return False
  