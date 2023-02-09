def round_sum(a, b, c):
    values = [int(round(i, -1)) for i in (a, b, c)]
    x=sum(values)
    return x