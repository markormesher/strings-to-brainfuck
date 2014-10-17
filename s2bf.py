import sys


current_cell_value = 0
current_cell = 0
output = ""


def get_cell_move_string(moveTo):
	pass


def change_value(changeTo):
	global current_cell_value, output

	# how far to move?
	difference = changeTo - current_cell_value

	# inefficient right now
	if (difference > 0):
		for i in range(0, difference):
			output += "+"
	elif (difference < 0):
		for i in range(0, (difference * -1)):
			output += "-"


def translate(input):
	global current_cell_value, output

	# loop all characters
	characters = list(input)
	for c in characters:
		# find the ASCII value for this colour
		required_char_val = ord(c)

		# apply the necessary changes
		change_value(required_char_val)

		# print the character
		output += "."

		# update our memory of the current cell value
		current_cell_value = required_char_val

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
