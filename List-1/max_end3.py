def max_end3(nums):
    x=nums[0]
    y=nums[-1]
    if x>y:
        a=[] 
        for i in range(len(nums)):
            a.append(x)    
        return a 
    else:
        b=[] 
        for j in range(len(nums)):
            b.append(y)  
        return b  