import turtle
import os
import math
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
turtle.register_shape("alien.gif")
turtle.register_shape("cannon.gif")

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

number_of_enemies = 2
enemies = []


for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:   
    enemy.color("red")
    enemy.shape("alien.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2



bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() -t2.xcor(),2)+ math.pow(t1.ycor() -t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:

    for enemy in enemies:
        x = enemy.xcor()
        enemy.setx(x)

        if isCollision(bullet, enemy):

            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)        



        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle
            print("Game Over")
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

        

    


