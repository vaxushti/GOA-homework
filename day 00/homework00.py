from turtle import *



#we want to paint a house
speed(10)
width(10)
#step 1:

forward(200)
left(90)

forward(200)
left(90) 

forward(200)
left(90) 

forward(200)
left(90) 

#end of square

#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
 
penup() 
goto(0,0)
pendown()

 # drawing window1 

 

penup()
goto(200, 200)
pendown ()

right(-30)
forward(60)
color("blue")
right (90)
forward (50)
left(90)
forward(50)
left(90)
forward(50)
left (90)
forward(25)
left (90)
forward(50)
left(90)
forward(25)
right(-90)
forward(25)
left(90)
forward(50)

penup()
goto(0,0)
pendown()


right(-0)
color("blue")
forward(90)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)

penup()
goto(180,230)
pendown()

color("brown")
begin_fill()
forward(100)
left(90)
forward(30)
left(90)
forward(55)
end_fill()


penup()
goto(750,-0)
pendown()
color("green")
begin_fill()
right(90)
forward(1600)
left(90)
forward(500)
left(90)
forward(1600)

end_fill()

penup()
goto(750,350)
pendown()

color("blue")
begin_fill()
right(180)
forward(1600)
right(90)
forward(150)
right(90)
forward(1600)
end_fill()

penup()
goto(-100,100)
pendown()


exitonclick()