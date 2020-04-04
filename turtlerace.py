import random
from turtle import *
import math
import time
# set the window size
win_length = 250
win_height = 250
# essentially the turtles have the name of their color
turtles = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'white', 'grey']
colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'white', 'grey']
# function for a 360 degree turn to the left
def turn():
    for turn in range(60):
        turtles[i].left(6)
# function for a 360 degree turn to the right
def win():
    for win in range(60):
        turtles[i].right(6)
# screen
screensize(win_length, win_height, "lightgreen")
penup()
# variables
i = 0
done = False
ycoord = win_length * 0.5 - win_length * 0.1
ycoordtrack = win_height * 0.5 - win_height * 0.05 + win_height * 0.05
# draws the race track
goto(-240, ycoordtrack)
for step in range(16):
  write(step, align='center')
  right(90)
  for num in range(12):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(240) # 20 times the range
  left(90)
  forward(20)
# draws the racers
while i <= 8: 
    turtles[i] = Turtle()
    turtles[i].color(colors[i])
    turtles[i].shape('turtle')
    turtles[i].penup()
    turtles[i].goto(-240, ycoord)
    turtles[i].pendown()
    turn()
    i = i + 1
    ycoord = ycoord - 25
# the race loop
for turn in range(1000):
    turtles[random.randint(0,8)].forward(random.randint(1,5))
    i = 0
    while i <= 8:
        if (turtles[i].xcor() > 50):
            #print('%s has won' % (colors[i])) # in terminal
            style = ('Comic Sans MS', 30, 'bold') # font
            Turtle().write('%s has won' % (colors[i]), font=style, align='center') # writes on screen
            done = True
            break
        i = i + 1
    if done:
        win()
        break
time.sleep(5) # timer to display the results