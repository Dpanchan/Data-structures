def last_index(arr, target):
  for i in range(len(arr)-1, -1, -1): #start from last index nunchi 0 index varaku,-1 vachi ekada agali ani
    if arr[i] == target:
      return i

d = [1, 2, 4, 3, 6, 5, -1, -2, 0, 4, 3, 4, 4]
index = last_index(d, 4)
print index
assert index == len(d)-1
