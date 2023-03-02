from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clearBoard():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forwards,key="w")
screen.onkey(fun=move_backwards,key="s")
screen.onkey(fun=move_left,key="a")
screen.onkey(fun=move_left,key="d")
screen.onkey(fun=clearBoard ,key="c")
screen.exitonclick()
