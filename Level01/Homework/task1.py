from turtle import *




speed(25)
width(7)
color("orange")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

begin_fill()

forward(70)
color("black")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

end_fill()

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200, 160)
pendown()
color("cyan")

begin_fill()

right(60)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(0, 160)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()