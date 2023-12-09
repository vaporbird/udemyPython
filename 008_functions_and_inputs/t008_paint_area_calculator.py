#just having fun
from math import ceil as ceil
def calc_needed_paint_for_wall(length, width, paint_coverage_per_can):
	return int(ceil((length*width)/paint_coverage_per_can))

print("You will need " + str(calc_needed_paint_for_wall(\
length = float(input("What is the length of the wall: ")),\
width = float(input("What is the width of the wall: ")),\
paint_coverage_per_can = float(input("How many sqr meters per can of paint? "))\
)) + " cans of paint!")
