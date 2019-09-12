def binary_search(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) / 2
    print "looking for", target, "mid value:", arr[mid], "low", low, "high", high, "mid", mid
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      # arr[mid] > target
      high = mid - 1
  return -1
   
d = [-3, -2, -1, 0, 1, 1, 2, 3, 4, 5, 6, 10]

test_cases = (-3, -2, -1, 0, 1, 3, 4, 7, 9, 10) 
for number in test_cases:
  index = binary_search(d, number)
  if index != -1:
    print d[index], "==", number, "?", d[index] == number
  else:
    print number, "was not in the list"
