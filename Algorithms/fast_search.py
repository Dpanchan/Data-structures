from pprint import pprint as pp

def fast_search(arr, target):
  new = {}
  count = 0
  li = []
  for index, i in enumerate(arr):
    if i == target:
      li.append(index)
      new[i] = li
    count += 1
  return (-1 if not li else li[0]), count
      
   
d = [-3, -3, -1, 0, 1, 1, 1, 2, 3, 4, 5, 6, 10]

test_cases = (-3, -2, -1, 0, 1, 3, 4, 7, 9, 10) 
for number in test_cases:
  index, count = fast_search(d, number)
  if index != -1:
    print d[index], "==", number, "?", d[index] == number, count
  else:
    print number, "was not in the list", count
