def memoize(func):
    kesh = {}

    def inner(n):
        if n not in kesh.keys():
            print("Результат виконання функції")
            kesh[n] = func(n)
            return kesh[n]
        else:
            print("Результат взято з кешу")
            print(kesh[n])
            return kesh[n]
    return inner


@memoize
def faktorial(n):
    rez = 1
    for i in range(1, n):
        rez *= i
    print(rez)
    return rez


faktorial(5)
print(100 * '*')
faktorial(5)
print(100 * '*')
faktorial(4)
print(100 * '*')
