a = int(input())
b = int(input())
c = int(input())

test = b**2-4*a*c
if test > 0:
    x1 = (-b + (b**2-4*a*c)**0.5) / 2 * a
    x2 = (-b - (b**2-4*a*c)**0.5) / 2 * a
    print(x1)
    print(x2)

elif test == 0:
    x = -b / 2 * a
    print(x)

else:
    print("XXXXXXX")

