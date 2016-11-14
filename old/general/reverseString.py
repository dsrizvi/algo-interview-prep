
def reverse(string):
	length = len(string) - 1
	result = ''
	for i in range(length + 1):
		result += string[length - i]
	return result


def recursiveReverse(input_string):
	if len(input_string) == 0:
		return input_string
	else:
		print input_string, input_string[0]
		return recursiveReverse(input_string[1:]) + input_string[0]




def main():
	print reverse("string")
	print recursiveReverse('string')

if __name__ == '__main__':
	main()