import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
for _ in range(4):
    board.forward(100)
    board.left(90)
    
board.penup()
board.forward(50)
board.right(90)
board.forward(100)
board.pendown()

for _ in range(4):
    board.forward(100)
    board.right(90)

turtle.done()