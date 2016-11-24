

def print_ord(s):
	print(s)
	ords = ''
	for c in list(s):
		print(c + ' ' + str(ord(c)))


def main():
	print_ord('dhck')
	print_ord('dhkc')


if __name__ == '__main__':
	main()