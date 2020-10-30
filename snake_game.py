import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0


# set up the screen
wn = turtle.Screen()
wn.title("snake game by KH")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("dark blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("dark violet")
food.penup()
food.goto(0,100)


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# functions
def up():
    if head.direction !="down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction =="up":
        head.sety(head.ycor()+20)

    elif head.direction =="down":
        head.sety(head.ycor()-20)

    elif head.direction =="left":
        head.setx(head.xcor()-20)

    elif head.direction =="right":
        head.setx(head.xcor()+20)

# keyboard bindings
wn.listen()
wn.onkeypress(up, 'Up')
wn.onkeypress(down, 'Down')
wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')

segments=[]

# main game loop
while True:
    wn.update()

    # check for a collision with the border
    if head.xcor()>290:
        head.goto(head.xcor()-600,head.ycor())

    elif head.xcor()<-290:
        head.goto(head.xcor() + 600, head.ycor())

    elif head.ycor()>290:
        head.goto(head.xcor(), head.ycor()-600)

    elif head.ycor() < -290:
        head.goto(head.xcor(), head.ycor()+600)


    # check for collision with the food
    if head.distance(food)<20:
        # move the food to random place
        food.goto(random.randint(-290,290),random.randint(-290,290))

        # add a segment
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("light blue")
        new_segment.penup()
        segments.append(new_segment)

        delay-=0.001
        score+=10

        if score>high_score:
            high_score=score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # move the segments
    for index in range (len(segments)-1,0,-1):
        segments[index].goto(segments[index-1].xcor(),segments[index-1].ycor())

    # move segment 0 to where the head is
    if len(segments) > 0:
        segments[0].goto(head.xcor(),head.ycor())

    move()


    # check for collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"


            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)



if __name__=='__main__':
    wn.mainloop()
