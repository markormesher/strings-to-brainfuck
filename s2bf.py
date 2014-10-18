import sys
import math


# cell locations
COUNTER_CELL = 0
OUTPUT_CELL = 1


current_cell_value = 0
current_cell = 0
output = ""


def move_to_cell(moveTo):
	global current_cell, output

	# how far to move
	difference = moveTo - current_cell

	# move!
	if (difference > 0):
		for i in range(0, difference):
			output += ">"
	elif (difference < 0):
		for i in range(0, (difference * -1)):
			output += "<"

	# update current location
	current_cell = moveTo


def change_value(changeTo):
	global current_cell_value, output

	# how far to move?
	difference = changeTo - current_cell_value
	if (difference == 0):
		pass
	elif (difference > 0):
		moveChar = "+"
	else:
		difference = difference * -1
		moveChar = "-"

	# pick which method to use
	if (difference >= 16):
		# use a loop to change by the biggest square number smaller than the target, then adjust

		# move into the loop counter and set it up
		move_to_cell(COUNTER_CELL)
		root = int(math.floor(math.sqrt(difference)))
		for i in range(0, root):
			output += "+"

		# create the loop section: move to output, increase, back to counter, decrease
		output += "["
		move_to_cell(OUTPUT_CELL)
		for i in range(0, root):
			output += moveChar
		move_to_cell(COUNTER_CELL)
		output += "-]"
		move_to_cell(OUTPUT_CELL)

		# add on anything missed in the loop
		extra = difference - (root * root)
		for i in range(0, extra):
			output += moveChar
	else:
		# inefficient linear method
		for i in range(0, difference):
			output += moveChar

	# update current cell value
	current_cell_value = changeTo


def translate(input):
	global current_cell_value, output

	# loop all characters
	characters = list(input)
	for c in characters:
		# find the ASCII value for this character
		required_char_val = ord(c)

		# apply the necessary changes
		change_value(required_char_val)

		# make sure we're on output
		move_to_cell(OUTPUT_CELL)

		# print the character
		output += "."

	# return the BF
	return output


def main():
	if (len(sys.argv) == 2):
		print translate(sys.argv[1])
	else:
		print("Invalid arguments supplied")
		print("Usage: " + sys.argv[0] + " \"String to translate\"")
		print("       OR")
		print("       " + sys.argv[0] + " \"String to translate\" > outputfile.bf")

if (__name__ == "__main__"):
	main()
