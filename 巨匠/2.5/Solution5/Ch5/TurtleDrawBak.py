import turtle

p = turtle.Turtle()
p.penup()
p.goto(-50, -50)
p.pendown()
sides = int(input('繪製正N邊形, 輸入N:'))
angle = 360/sides
print(angle)

for i in range(sides):    
    p.forward(100)
    p.left(angle)


p.clear()
p.reset()
circleNum = int(input('繪製N個同心圓, 輸入N:'))
for i in range(1, circleNum+1):
    p.penup()
    p.backward(25)
    p.right(90)
    p.pendown()
    p.circle(25*i)
    p.left(90)
  
##p.clear()
##p.reset()
##sides = int(input('繪製正N角星, 輸入N:'))
##angle = 180+180/sides
##print(angle)
##for p in range(sides):
##    p.forward(100)
##    p.right(angle)
##
