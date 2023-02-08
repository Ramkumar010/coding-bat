def front_times(string, n):
    string1=""
    if len(string)>3:
        for i in range (n):
            string1=string1+string[0:3]
        return string1
    else:
        for i in range (n):
            string1=string1+string
        return string1   
    