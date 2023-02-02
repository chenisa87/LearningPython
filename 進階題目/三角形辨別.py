"""
若 a + b ≦ c ，三線段無法構成三角形
若 a × a + b × b < c × c ，三線段構成鈍角三角形(Obtuse triangle)
若 a × a + b × b = c × c ，三線段構成直角三角形(Right triangle)
若 a × a + b × b > c × c ，三線段構成銳角三角形(Acute triangle)
"""
numbers = input()
numbers = list(int(n) for n in numbers.split(" "))
numbers.sort()
a = numbers[0]
b = numbers[1]
c = numbers[2]

def check():
    if a + b <= c:
        return "No"
    elif a*a + b*b < c*c:
        return "Obtuse"
    elif a*a + b*b == c*c:
        return "Right"
    elif a*a + b*b > c*c:
        return "Acute"
print("%d %d %d"%(a,b,c))
print(check())