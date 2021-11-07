def summation(num):
    i = 0
    n = 0
    for i in range(num + 1):
        n += i
        i += 1
    return n

print(summation(5))