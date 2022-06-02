list = [a+5*(a-1) for a in range(10)]
b = iter(list)
while b:
    try:
        print (next(b))
    except:
        break