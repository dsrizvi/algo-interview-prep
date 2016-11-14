def combinations(mappings, number):

	letters = [mappings.get(digit) for digit in number]

	for A in letters:



def main():
	mappings = {"1":["A","B","C"], "2":["D","E","F"]}
	print combinations(mappings, "21")

if __name__ == '__main__':
	main()
