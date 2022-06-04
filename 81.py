l = [i%3 for i in range(10)]
print(l)
# it = ITER(l)
while it:
    try:
        print (next(it))
    except:
        break