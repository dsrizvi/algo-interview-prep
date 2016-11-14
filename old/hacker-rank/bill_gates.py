n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
min_diff = []

min_diff = min([candies[x + k -1] - candies[x] for x in range(0,n - k + 1)])

print min_diff
