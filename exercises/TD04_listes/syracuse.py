n = 3
# n * 3 + 1 = 9
# 9 * 3 + 1 = 28
# 28 / 2 = 14
# 14 / 2 = 7
def syracuse (n) :
    while n > 1 :
     n = n
    if n % 2 != 0 :
        n = n * 3 + 1
    elif n % 2 == 0 :
        n = n / 2
    return n
print (syracuse (2))



