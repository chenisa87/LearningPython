a,b,c = eval(input("Enter a,b,c"))
d,e,f = eval(input("Enter d,e,f"))

if a*e - b*d ==0:
    if c*e - b*d == 0 and a*f - c*f == 0:
        print("有無限多組解")
    else:
        print(("無解"))
else:
    x = (c*e - b*f) / (a*e - b*d)
    y = (a*f - c*d) / (a*e - b*d)
    print("x is %.2f, y = %.2f "%(x,y))