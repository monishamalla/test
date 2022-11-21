def ternary(n):
    e = n//3
    q = n%3
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e) + str(q)
        
num=int(input("Enter a number: "))
print(ternary(num))
