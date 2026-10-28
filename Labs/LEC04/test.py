import turtle
import random

def drunken_move():
    turtle.setheading(random.randint(0, 360))
    turtle.forward(random.randint(100,200))
    turtle.stamp()

turtle.shape('turtle')
# 원본: while (True):
# 웹 실습에서는 종료할 수 있도록 아래 한 줄만 변경
for i in range(5):
    drunken_move()