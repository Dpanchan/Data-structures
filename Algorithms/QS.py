def quick_sort(l):
  if l[1:]:
    p = l[0]
    return (
      quick_sort([x for x in l if x < p]) +
      [x for x in l if x == p] +
      quick_sort([x for x in l if x > p]))
  return l


l = [3,2,5,1,7]
print(quick_sort(l))



# 0,1,2,3,5,6,7

#  64
# 32 32
# 16 16
# 8 8 
# 4 4 
# 2 2 
# 1 1
