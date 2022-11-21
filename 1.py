def ternary(n):
    a = n//3
    b = n%3
    if n == 0:
        return '0'
    elif a == 0:
        return str(b)
    else:
        return ternary(a) + str(b)
        
num=int(input("Enter a number: "))
print(ternary(num))
