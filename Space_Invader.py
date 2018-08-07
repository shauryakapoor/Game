# Just a fun little game using python 
# I did not create this game from scratch
# I found a couple of youtube tutorials and then modified it. 

import turtle
import os 

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Invaders")

#Draw borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#The player 
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#delay = input("Press enter to finish")

playerspeed = 15

#Create the enemy 
enemy = turtle.Turtle()
enemy.color("orange")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)


enemyspeed = 2

#Move the player left and right 
def move_left():
    x = player.xcor()
    if x < -280:
        x = -280 
    x -= playerspeed
    player.setx(x)

def move_right():
    x = player.xcor()
    if x > 280:
        x = 280 
    x += playerspeed
    player.setx(x)

#Create keyboard bindings 
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

#Main game loop 
while True: 


    #Move the enemy 
    x = enemy.xocr()
    x += enemyspeed
    enemy.setx(x)

wn.mainloop()


