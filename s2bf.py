import sys


def get_value_change_string(value):
	output = ""

	# inefficient right now
	if (value > 0):
		for i in range(0, value):
			output += "+"
	elif (value < 0):
		for i in range(0, (value * -1)):
			output += "-"

	# finish
	return output


def translate(input):
	output = ""
	characters = list(input)
	current_cell_value = 0

	# loop all characters
	for c in characters:
		# find the ASCII value for this colour
		required_char_val = ord(c)

		# work out how far we need to move from the current value
		difference = required_char_val - current_cell_value

		# apply the necessary changes
		output += get_value_change_string(difference)

		# print the character and update our memory of the current cell value
		output += "."
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
