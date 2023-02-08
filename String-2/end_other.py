def end_other(a, b):
    x=len(a)
    y=len(b)
    a=a.lower()
    b=b.lower()
    if x<y:
        if b.endswith(a):
            return True
        else:
            return False
    if x>y:
        if a.endswith(b):
            return True
    if x==y:
        if a.endswith(b):
            return True
        else:
            return False
    else:
            return False