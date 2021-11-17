n = 3
# n * 3 + 1 = 10
# 10 / 2 = 5
# 5 *3 + 1 = 16
# 16 / 2 = 8
def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    results = [n]
    while n != 1 :
        if n % 2 != 0 :
            n = n * 3 + 1
            results.append (n)
        elif n % 2 == 0 :
            n = n // 2
            results.append (n)
    return results
print(syracuse(3))




