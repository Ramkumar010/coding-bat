def extra_end(string):
    if len(string)>1:
        x=string[-1]
        y=string[-2]
        string1=y+x
        new_string=string1+string1+string1
        return new_string
    