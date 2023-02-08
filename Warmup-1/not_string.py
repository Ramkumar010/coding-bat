def not_string(string):
    if string.startswith("not"):
        return string 
    else:
        return ("not"+" "+ string)    