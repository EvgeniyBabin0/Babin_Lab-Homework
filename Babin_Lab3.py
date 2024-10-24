def min_breaks(n,m):
    if n==1 and m==1:
        return 0
    elif n==1:
        return m-1
    elif m==1:
        return n-1
    else:
        return n*m-1
n=int(input("Введите значение (n): "))
m=int(input("Введите значение (m): "))
result=min_breaks(n,m)
print(f"Минимальное кол-во разломов для шоколадной плитки {n}x{m}: {result}")
