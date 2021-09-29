import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0

bodies = []

# Box Where snake will run
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)

# Creating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

# Score Board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score: 0 | Highest Score: 0")

# Moving snake

def moveup():
      if head.direction != "down":
            head.direction="up"
def movedown():
      if head.direction != "up":
            head.direction="down"
def moveright():
      if head.direction != "left":
            head.direction = "right"
def moveleft():
      if head.direction != "right":
            head.direction = "left"
def movestop():
      head.direction = "stop"

def move():
      if head.direction=="up":
            y = head.ycor()
            head.sety(y+20)
      if head.direction=="down":
            y = head.ycor()
            head.sety(y-20)
      if head.direction=="left":
            x = head.xcor()
            head.setx(x-20)
      if head.direction=="right":
            x = head.xcor()
            head.setx(x+20)

# Key Handle
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

while True:
      s.update()
      if head.xcor()>290:
            head.setx(-290)
      if head.xcor()<-290:
            head.setx(290)
      if head.ycor()>290:
            head.sety(-290)
      if head.ycor()<-290:
            head.sety(290)

            # Eating Food
      if head.distance(food)<20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            body = turtle.Turtle()
            body.speed(0)
            body.penup
            body.shape("square")
            body.color("red")
            body.fillcolor("black")
            body.append(body)

            # Increment Score
            score += 10
            delay = 0.001

            if score>highestscore:
                  highestscore=score
            sb.clear()
            sb.write("Score: {} Highest Score: {}".format(score,highestscore))

            for index in range(len(bodies)-1,0,-1):
                  x = bodies[index-1].xcor()
                  y = bodies[index-1].ycor()
                  bodies[index].goto(x,y)
            if len(bodies)>0:
                  x = head.xcor()
                  y = head.ycor()
                  bodies[0].goto(x,y)
            move()

            # if snake bodies touched
            for body in bodies:
                  if body.distance(head)<20:
                        time.sleep(1)
                        head.goto(0,0)
                        head.direction = "stop"

                        for body in bodies:
                              body.ht()
                        bodies.clear()
                        score = 0
                        delay = 0.1

                        sb.clear()
                        sb.write("Score: {} Highest Score: {}".format(score, highestscore))
            time.sleep(delay)
      s.mainloop()



# Other Game

"""
from turtle import Turtle

turtle = Turtle()
turtle.hideturtle()
turtle.speed('fastest')
turtle.pensize(3)

turtle.penup()
turtle.sety(-100)  # center circle on screen
turtle.pendown()
turtle.circle(100)

circle = input("What shape is this? - ").lower()

while circle != 'circle':
    print("That's not the right shape.")
    circle = input("What shape is this? - ").lower()

print("Good Job!")

turtle.clear()

turtle.penup()
turtle.goto(-25, -25)  # center square on screen
turtle.pendown()

for _ in range(4):
    turtle.forward(50)
    turtle.left(90)

sq = input("What shape is it? - ").lower()

while sq != 'square':
    print("That's not the right shape.")
    sq = input("What shape is it? - ").lower()

print("Good Job!")

"""






































