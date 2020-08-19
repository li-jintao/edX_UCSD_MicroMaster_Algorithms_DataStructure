# python3


def build_heap(data):
	"""Build a heap from ``data`` inplace.

	Returns a sequence of swaps performed by the algorithm.
	"""
	# The following naive implementation just sorts the given sequence
	# using selection sort algorithm and saves the resulting sequence
	# of swaps. This turns the given array into a heap, but in the worst
	# case gives a quadratic number of swaps.
	#
#	for i in range(len(data)):
#		for j in range(i + 1, len(data)):
#			if data[i] > data[j]:
#				swaps.append((i, j))
#				data[i], data[j] = data[j], data[i]
#	return swaps
	swaps = []
	start_index = int(len(data)/2)
	change = True
	while change:
		swaps, data, change = heapfy(swaps, data, start_index)
	return swaps

def heapfy(swaps, data, start_index):
	change = False
	for i in reversed(range(0, start_index)):
		children_index = [(i+1)*2-1, (i+1)*2]
		children = [data[(i+1)*2-1]]
		if len(data) > children_index[1]:
			children.append(data[(i+1)*2])
		if min(children) < data[i]:
			jj = children.index(min(children))
			j = children_index[jj]
			swaps.append((i, j))
			data[i], data[j] = data[j], data[i]
			change = True
	return swaps, data, change
		

def main():
	n = int(input())
	data = list(map(int, input().split()))
	assert len(data) == n

	swaps = build_heap(data)

	print(len(swaps))
	for i, j in swaps:
		print(i, j)
	# print(data)

if __name__ == "__main__":
	main()
