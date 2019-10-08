directions = "L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R2, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1"
from turtle import*
from math import *
setup()
speed(0)

dir_list = directions.split(", ")


for direction in dir_list:
    if "L" in direction:
        direction_num = int(direction.replace("L",""))
        left(90)
        forward(direction_num)
    if "R" in direction:
        direction_num = int(direction.replace("R",""))
        right(90)
        forward(direction_num)

p = pos()
print(p)
sum_p = int(1+(p[0]+ p[1]))
if sum_p % 69 == 0:
    print(sum_p ,"/", 69 ,"=", sum_p/69 )
