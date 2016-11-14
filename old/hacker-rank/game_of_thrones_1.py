string = raw_input()

string_set = set(string)
# print string_set
char_count = []

for char in string_set:
	char_count.append(string.count(char))

odd_numbers = [n for n in char_count if n%2==1]
# print odd_numbers
if len(odd_numbers) <= 1:
	print True
else:
	print False	