def centered_average(nums):
    smallest = min(nums)
    biggest = max(nums)
    x=(sum(nums) - smallest - biggest) 
    y=len(nums)-2
    total=x/y
    return total