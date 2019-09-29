from turtle import *

# set width and height to labyrinth size
setup(600,600)
# set the labyrinth as background
bgpic('labyrinth.png')
# show the cursor
shape()
# increase speed to maximum
speed(0)



# # Start bis Diagonale # #

# Block 1

right(180)
forward(65)
right(90)

# Block 2 

forward(50)
right(90)
forward (25)
left(90)

# Nameblock

forward (31)
right (90)
write("martk4",font=("Arial", 30, "normal"))
forward (150)

# Block 3

left (90)
forward (30)
right(90)
forward(50)

# Block 4

left (90)
forward (32)

# Dollarblock

left(90)
forward (3)
dot(15)
forward (21)
dot(15)
right(90)
forward(22)
dot(15)
right(90)
forward(21)
dot(15)
right(90)
forward(22)
left(90)
forward(3)
right(90)
forward(32)

# Block 4 return

right(90)
forward(50)
left(90)
forward(30)

# Block 3 & Nameblock return

right(90)
forward(182)
right(90)
forward(22)
left(90)
forward(58)

# Diagonale

for i in range(132):
    right(90)
    forward(1)
    left (90)
    forward(1)

# Upper Boxes left half

right(180)
forward(24)
left(90)
forward (3)
dot(15)
forward(30)

right(90)
forward(50)
right(90)
forward (34)
left(90)
forward(50)
left(90)
forward(34)
right(90)
forward(50)
right(90)
forward (34)
left(90)
forward(50)
left(90)
forward(34)
right(90)
forward(50)
right(90)
forward (3)
dot(15)
forward (33)
left(90)
forward (25)

# Upperboxes left half

left(90)
forward(34)
right(90)
forward(50)
right(90)
forward (34)
left(90)
forward(50)
left(90)
forward(34)
right(90)
forward(50)
right(90)
forward (34)
left(90)
forward(48)
left(90)
forward (32)
dot(15)

# right side boxes

right(90)
forward (32)
right(90)
forward (50)
right(90)
forward(31)
dot (15)
forward(2)
left (90)

forward(50)
left(90)
forward(32)
right(90)
forward (50)
right(90)
forward(32)
left (90)
forward (50)

left (90)
forward(32)
right(90)
forward(50)
right(90)
forward (30)
dot(15)
left(90)
forward (10)
left(90)
forward(27)
right(90)
forward (16)
dot(15)

right(90)
forward (30)
left(90)
forward(50)
left(90)
forward(32)
right(90)
forward (50)
right(90)
forward(32)
left(90)
forward(50)
left(90)
forward(32)
right(90)
forward (50)
right(90)
forward(32)
left(90)
forward(30)
right(90)
forward(32)
right(90)
forward (160)

# Circle

left(90)
forward(50)

for i in range (13):
    forward(4)
    left(90)
    forward(1)
    right(90)

for i in range (21):
    forward(3)
    left(90)
    forward(2)
    right(90)

for i in range (21):
    forward(2)
    left(90)
    forward(3)
    right(90)

for i in range (17):
    forward(1)
    left(90)
    forward(4)
    right(90)

forward (72)

for i in range (13):
    forward(4)
    right(90)
    forward(1)
    left(90)

for i in range (22):
    forward(3)
    right(90)
    forward(2)
    left(90)

for i in range (21):
    forward(2)
    right(90)
    forward(3)
    left(90)

for i in range (17):
    forward(1)
    right(90)
    forward(4)
    left(90)

# finish

right (90)
forward (50)
right(90)
forward(40)
left (90)
forward (10)
right (90)
forward (60)
right (90)
forward (39)
left (90)
forward(32)
dot(15)




exitonclick()
