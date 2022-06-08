n = int(input('Введіть число: '))
k = 2
f = False
while n > 0:
    if n % 10 == k:
       f = True
       break
    n //=10
if f:
    print('Yes')
else:
     print("No")
