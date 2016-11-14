def validCat(dictionary, string):

	if len(string) == 0:
		return True

	for i in range(len(string)+1):
		if string[:i] in dictionary:
			if validCat(dictionary,string[i:]):
				return True
	return False

def main():
	dictionary = {'world':'', 'hello':'', 'super':'', "hell":''}
	print validCat(dictionary, 'helloworld')

if __name__ == '__main__':
	main()