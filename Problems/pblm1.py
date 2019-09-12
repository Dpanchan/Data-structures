def twi(arr):
	mini = arr[0]
	for i in range(len(arr)):
		if arr[i]<arr[i+1]:
			mini = arr[i]
		return mini
arr = [4,5,6,-2]
print twi(arr)
