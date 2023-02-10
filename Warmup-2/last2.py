def last2(string):
    if len(string)>2:
        x=string[-2]+string[-1]
        count=0
        for i in range (len(string)-1):
            if string[i]+string[i+1]==x:
                count=count+1
        return count-1
    else:
        return 0
        
