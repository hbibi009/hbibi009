import turtle

turtle.speed(3)

# 얼굴
turtle.color('yellow')
turtle.penup()
turtle.goto(0, -85)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#왼쪽 눈
turtle.penup()
turtle.goto(-20, 40)
turtle.pendown()
turtle.color('black')
turtle.dot(15)

#오른쪽 윙크
turtle.pensize(4)
turtle.penup()
turtle.goto(15, 35)
turtle.setheading(60)
turtle.pendown()
turtle.circle(-10, 110)

#입
turtle.penup()
turtle.goto(-40, 0)
turtle.setheading(-60)
turtle.pendown()
turtle.circle(46, 120)

turtle.hideturtle()
turtle.done()
