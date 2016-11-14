def move(array):
    start = 0;
    end = len(array)-1;

    zero_index = []

    while start != end:
        while start != 0:
            start += 1
        while end == 0:
            end -= 1
        i = start
        while i != end:
            array[i], array[i+1] = array[i+1], array[i]
            print array[i]
            i += i

    return array


def main():
	print(move([1, 0, 6, 0, -4, 2, 5, 1]))  # [1, 6, -4, 2, 5, 1, 0, 0]
	print(move([1, 2, 3, 4, 5, 6, 7, 8]))   # [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == '__main__':
	main()