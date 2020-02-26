def a(x, current=0, xsum=0):
    if current < x:
        current+=1
        xsum+=current
        a(x, current, xsum)
    else: print(xsum)

a(4)
