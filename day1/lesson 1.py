from turtle import*
shape('turtle')

#house

# draw a square
speed(3)
width(7)
color('blue')
begin_fill()
forward(200)
left(90)
end_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

# drawing a door
forward(70)
color('yellow')
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of door

penup()
goto(200,200)
pendown()

color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

#drawing a window 1
color('black')
begin_fill()
penup()
goto(50,70)
pendown()
right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()


#drawing window 2
begin_fill()
penup()
goto(150,70)
pendown()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()



exitonclick()
