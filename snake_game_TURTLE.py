import turtle as tt
import time as tm
import random as rn
import tkinter as tk

delay = 0.175
score = 0
hscore = 0
seg = []


# Main Window
wnd = tt.Screen()
wnd.title("Snake Game by @Shriyansh_47")
wnd.bgcolor("black")
wnd.setup(width=700, height=700) # Dimensions of the window
wnd.tracer(0) # Turns of screen updates


# Snake Head
thead = tt.Turtle()
thead.speed(0) # This sets the drawing speed of the turtle, the speed at which the turtle head draws.
               # 0 or "fastest" -> No animation while drawing (instant drawing)
               # 1 or "slowest" -> slowest
               # 10 or "fast" -> fast
thead.shape("square")
thead.color("white")
thead.penup() # Turtles when move draw line, .penup() prevents drawing of line
thead.goto(0,0) # by default tutle starts at (0,0)
                # (0,0) is at the centre of screen like coordinate axis
                # .goto(x,y) moves the tutle to desired coordinate from (0,0)
                # since penup() therefore no line would get drawn
thead.direction = "stopped"


# Snake Food
fhead = tt.Turtle()
fhead.speed(0)
fhead.shape("circle")
fhead.color("red")
fhead.penup()
fhead.goto(147,0)

# Play Arena
brhead = tt.Turtle()
brhead.hideturtle()
brhead.color("white")
brhead.shape("square")
brhead.pensize(1)
brhead.penup()
brhead.goto(-250,250)
brhead.pendown()
for i in range(4):
    brhead.forward(500) # Move forwards by 500px
    brhead.right(90) # Turn 90 degress to the right


# Death Message
dhead = tt.Turtle()
dhead.hideturtle()
dhead.speed(0)
dhead.color("red")
dhead.shape("square")
dhead.penup()
dhead.goto(0,0)

def death_message():

    #Throwing the main turtle head
    thead.goto(1000,1000)

    # Throwing the current Snake's segments out of screen / (couldnt find a way to del them)
    for i in seg:
        i.goto(1000,1000)
        
    # Clearing the segments
    seg.clear()

    # Throwing the food too
    fhead.goto(1000,1000)

    for i in range(3):
        dhead.write("You Died !", align="center", font=("OptimusPrincepsSemiBold", 40, "bold"))
        wnd.update()
        tm.sleep(0.3)
        dhead.clear()
        wnd.update()
        tm.sleep(0.2)
    
    dhead.write("You Died !", align="center", font=("OptimusPrincepsSemiBold", 40, "bold"))
    wnd.update()
    tm.sleep(1.5) # Delay between starting of new game and your Death
    dhead.clear()


# Scoring 
def score_display():
    shead.clear()
    shead.write(f"Score : {score}     High-Score : {hscore}", align="center", font=("Minecraft", 24, "normal"))


# Score Turtle
shead = tt.Turtle()
shead.speed(0)
shead.shape("square")
shead.color("white")
shead.penup()
shead.hideturtle()
shead.goto(0, 280)
score_display()


# Credits
name = tt.Turtle()
name.hideturtle()
name.color("white")
name.shape("square")
name.penup()
name.goto(133,-270)
name.write("@ Shriyansh_47", font=("OptimusPrincepsSemiBold", 12, "normal"))


# Collision Checks
def check_within_body():
    for i in seg:
        if i.distance(fhead) < 20:
            return True
    return False

def check_with_food():
    if thead.distance(fhead) < 20 or check_within_body(): # Note :- By default the size of a turtle is 20pxX20px, 
                                           # Therefore, if the distance between centre of thead & centre of fhead
                                           # is < 20 (20/2 + 20/2) 
                                           # we will randomly assign it a new psoition
        x = rn.randint(-240 , 240)
        y = rn.randint(-240 , 240)
        fhead.goto(x, y)

        # Adding new body segments
        new_seg = tt.Turtle()
        new_seg.shape("square")
        new_seg.speed(0)
        new_seg.penup()
        seg.append(new_seg)

        colors = ["#00008B", "#0000CD", "#0000FF", "#1E90FF", "#4169E1",
                 "#4682B4", "#5F9EA0", "#6495ED", "#87CEEB", "#87CEFA",
                 "#ADD8E6", "#B0E0E6", "#E0FFFF", "#F0F8FF", "#F8F8FF"]
        
        new_seg.color(colors[(len(seg)-1)% len(colors)])

        global score
        global hscore
        global delay

        score += 10
        hscore = max(score,hscore)
        score_display()

        delay -= 0.01 - (len(seg) % 10) * 0.001


def reset():
        death_message()

        thead.goto(0,0)
        thead.direction = "stopped"

        # Displacing the food too
        fhead.goto(rn.randint(-240,240), rn.randint(-240,240))

        global score
        global delay

        score = 0
        score_display()

        delay = 0.175


def check_with_wall():
    if thead.xcor() + 10 > 250 or thead.xcor() - 10 < -250 or thead.ycor() + 10 > 250 or thead.ycor() - 10 < -250:
        reset()


def check_with_body():
    for i in seg:
        if i.distance(thead) < 20:
            reset()


# Segment Movement
def seg_move():
    for i in range(len(seg)-1, 0, -1):
        x = seg[i-1].xcor()
        y = seg[i-1].ycor()
        seg[i].goto(x,y)

    if len(seg) > 0:
        x = thead.xcor()
        y = thead.ycor()
        seg[0].goto(x,y)
    

# Head Directions
def go_up():
    if len(seg) == 0:
        thead.direction = "up"
    if thead.direction != 'down':
        thead.direction = "up"
def go_down():
    if len(seg) == 0:
        thead.direction = "dpwn"
    if thead.direction != 'up':
        thead.direction = "down"
def go_right():
    if len(seg) == 0:
        thead.direction = "right"
    if thead.direction != 'left':
        thead.direction = "right"
def go_left():
    if len(seg) == 0:
        thead.direction = "left"
    if thead.direction != 'right':
        thead.direction = "left"


# Movement
def movement():
    if thead.direction == "up":
        y = thead.ycor() # Gets the current_y-coordinate
        thead.sety(y+20) # Sets the new_y-coordinate = current_y-coordinate + 20 (pixels)

    if thead.direction == "down":
        y = thead.ycor()
        thead.sety(y-20)
    
    if thead.direction == "right":
        x = thead.xcor()
        thead.setx(x+20)
    
    if thead.direction == "left":
        x = thead.xcor()
        thead.setx(x-20)


# Key Bindings
wnd.listen() # Enables the screen to listen for keyboard inputtings
wnd.onkeypress(go_up, "Up") # Calls go_up function when "w" key gets pressed
wnd.onkeypress(go_down, "Down")
wnd.onkeypress(go_left, "Left")
wnd.onkeypress(go_right, "Right")


# Main Game Loop
while True:
    wnd.update()
    check_with_wall()
    check_with_food()
    seg_move()
    movement()
    check_with_body()

    tm.sleep(delay)

wnd.mainloop()
