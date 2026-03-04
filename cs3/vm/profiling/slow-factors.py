n = 1000000000001
d = 2

while n > 1:
    if n % d:
        d += 1
    else:
        print(d)
        n //= d
