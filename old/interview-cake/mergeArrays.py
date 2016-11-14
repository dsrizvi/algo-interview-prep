def merge_arrays(a,b):
	i = 0
	j = 0
	merged = []
	while i < len(a) and j< len(b):
		if a[i] > b[j]:
			merged.append(b[j])
			j+=1
		else:
			merged.append(a[i])
			i+=1

	while i < len(a):
		merged.append(a[i])
		i+=1

	while j < len(b):
		merged.append(b[j])
		j+=1

	return merged


def main():
	my_array     = [3,4,6,10,11,15]
	alices_array = [1,5,8,12,14,19]
	print merge_arrays(my_array, alices_array)

if __name__ == '__main__':
	main()