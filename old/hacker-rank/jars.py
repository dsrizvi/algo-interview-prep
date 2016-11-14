N, M = [int(x) for x in raw_input().split()]
sum = 0
for _ in range(0,M):
	a, b, k = [int(x) for x in raw_input().split()]	 
	sum = sum + ((abs(a-b)+1)*k)

print int(sum/N)	