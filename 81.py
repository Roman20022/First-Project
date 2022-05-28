l = [i%3 for i in range(10)]
print(l)
it = iter(l)
while it:
    try:
        print(next(it))
    except:
        break