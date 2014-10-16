def translate(input):
	output = ""
	characters = list(input)
	current_cell_value = 0

	# loop all characters
	for c in characters:
		# find the ASCII value for this colour
		char_val = ord(c)

		# work out how far we need to move from the current value
		difference = char_val - cell_value

		# apply the necessary changes (very, very inefficiently)
		if (difference > 0):
			for i in range(0, difference):
				output += "+"
		elif (difference < 0):
			for i in range(0, (difference * -1)):
				output += "-"

		# print the character and update our memory of the current cell value
		output += "."
		cell_value = char_val

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
