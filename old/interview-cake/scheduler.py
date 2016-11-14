def merge_ranges(meetings):
	merged = []

	sorted_meetings = sorted(meetings)
	prev_start, prev_end = sorted_meetings[0]

	for cur_start, cur_end in sorted_meetings[1:]:
		if cur_start <= prev_end:
			prev_end = max(cur_end, prev_end)
		else:
			merged.append((prev_start,prev_end))
			prev_start, prev_end = cur_start, cur_end

	merged.append((prev_start, prev_end))

	return merged

def main():
	meetings =   [(3, 5), (0, 1), (4, 8), (10, 12), (9, 10)]
	print merge_ranges(meetings)

if __name__ == '__main__':
	main()