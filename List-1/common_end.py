def common_end(a, b):
    if len(a)>=1 and len(b)>=1:
        x=a[-1]
        y=b[-1]
        p=a[0]
        q=b[0]
        if x==y or p==q:
            return True
    return False 