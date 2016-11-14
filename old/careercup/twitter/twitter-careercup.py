# http://www.careercup.com/question?id=21249679
# For a technical phone screen: 

# Given a string "aaabbcccc", write a program to find the character with the second highest frequency.

def secondHighest(string):
	char_array = [0]*256

	for char in string:
		print ord(char)
		char_array[ord(char)]= char_array[ord(char)] + 1
	char_array[char_array.index(max(char_array))] = 0
	print chr(char_array.index(max(char_array)))		


def main():
 secondHighest("aaabbcccc")	



main()