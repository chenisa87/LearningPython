import turtle

def draw_square(a_turtle):
    for i in range(1,5):
        a_turtle.forward(100)
        a_turtle.right(90)

window=turtle.Screen()
window.bgcolor("grey")

sean = turtle.Turtle()
sean.shape('turtle')
sean.color('green')
draw_square(sean)

amy = turtle.Turtle()
amy.goto(0, 30)
amy.shape('arrow')
amy.color('red')
amy.circle(60)

window.exitonclick()
