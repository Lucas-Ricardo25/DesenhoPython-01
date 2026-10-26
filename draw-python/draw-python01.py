import turtle

caneta = turtle.Turtle()
tela = turtle.Screen()

tela.bgcolor("black")

caneta.color("red")
caneta.pensize(2)
caneta.speed(0)

for i in range(400):
    caneta.forward(i * 2)
    caneta.left(91)

turtle.done()