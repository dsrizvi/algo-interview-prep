
def merge(a,b):
	merged = []
	i, j = 0,0

	while i < len(a) and j<len(b):
		if a[i] <= b[j]:
			merged.append(a[i])
			i = i + 1
		else:
			merged.append(b[j])
			j = j + 1
	while i < len(a):
		merged.append(a[i])
		i = i + 1
	while j < len(b):
		merged.append(b[j])
		j = j + 1

	return merged


def main():
	print merge([1,5,7,8,11], [3,7,8,12,13,21] )

if __name__ == '__main__':
	main()