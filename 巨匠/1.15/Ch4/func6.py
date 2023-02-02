def weighted_sum(c, e=80, m=60):
    return (c+e*2+m*3)

x = weighted_sum(100, m=90)
print("x =", x)

y = weighted_sum(e=90, m=80, c=70)
print("y =", y)

z = weighted_sum(e=60, c= 80)
print("z =", z)

#w = weighted_sum(m=60, e= 80, 75)
#print("w =", w)
