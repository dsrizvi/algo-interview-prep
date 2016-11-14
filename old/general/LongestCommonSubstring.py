
def LCSlen(a ,b):
	if len(a) == 0 or len(b) == 0:
		return 0

	if a[-1] == b[-1]:
		return 1 + LCS(a[:-1], b[:-1])
	else:
		return max( LCS(a[:-1], b), LCS(a, b[:-1]))

def LCSlenDP(a,b):
	if len(a) == 0 or len(b) == 0:
		return 0
	m = len(a)
	n = len(b)
	T = [[0 for i in range(n+1)] for j in range(m+1)]

	for i,x in enumerate(a):
		for j,y in enumerate(b):
			if x == y:
				T[i+1][j+1] = T[i][j] + 1
			else:
				T[i+1][j+1] = max(T[i+1][j], T[i][j+1])
	return T[m][n]

def LCS(a ,b):
	if len(a) == 0 or len(b) == 0:
		return []

	if a[-1] == b[-1]:
		return [a[-1]] + LCS(a[:-1], b[:-1])
	else:
		return max( LCS(a[:-1], b), LCS(a, b[:-1]), key=len)

def LCSdp(a,b):
	if len(a) == 0 or len(b) == 0:
		return 0
	m = len(a)
	n = len(b)
	T = [[0 for i in range(n+1)] for j in range(m+1)]

	for i,x in enumerate(a):
		for j,y in enumerate(b):
			if x == y:
				T[i+1][j+1] = T[i][j] + 1
			else:
				T[i+1][j+1] = max(T[i+1][j], T[i][j+1])

	x,y = len(a), len(b)
	answer = []
	while x > 0 and y > 0:
		if T[x][y] == T[x-1][y]:
			x-=1
		elif T[x][y] == T[x][y-1]:
			y-=1
		else:
			answer = [a[x-1]] + answer
			x -= 1
			y -= 1

	return "".join(answer)

def main():
	s1 = "abcde"
	s2 = "abeabcde"
	print LCSdp(s1, s2)


if __name__ == '__main__':
	main()