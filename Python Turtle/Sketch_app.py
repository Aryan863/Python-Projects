import turtle


tim = turtle.Turtle()
screen = turtle.Screen()
tim.speed("fast")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear_screen():
    tim.home()
    tim.clear()
    


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)







screen = turtle.Screen()
screen.exitonclick()