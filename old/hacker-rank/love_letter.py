num_palindromes = input()


def match_char(a,b):
	return abs( ord(a) - ord(b) )	




for n in range(0,num_palindromes):

	palindrome = raw_input()
	len_palindrome = len(palindrome) - 1
	middle =  0 
	reduction = 0


	if len_palindrome%2 == 0:
		middle = int(round(len_palindrome/2))
		# print middle
	else:
		middle = len_palindrome/2	+ 1 


	for n in range(0,middle):
		if palindrome[n] != palindrome[len_palindrome - n]:
			reduction= reduction + match_char(palindrome[n], palindrome[len_palindrome-n])
		else:
			pass
	
	print reduction			



	
