import math

def kclosest(point, points, k):
    results = []

    distances = map(lambda (x,y) : [(distance(x,y, point)), x,y], points)
    distances.sort(key= lambda x : x[0])

    for i in range(k):
        results.append([distances[i][1], distances[i][2]])

    return results

def distance(a, b, point):
	return math.sqrt(math.pow(a-point[0],2) + math.pow(b-point[1],2) )




def main():
	points = ([-2, -4], [0, 0], [10, 15], [5, 6], (7, 8), [-10, -30])
	print kclosest([5,5],points, 2)

if __name__ == '__main__':
	main()


