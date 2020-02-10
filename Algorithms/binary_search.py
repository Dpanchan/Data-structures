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
   
# def binary_search(arr, i):
#   return arr.index(i) if i in arr else -1

d = [-3, -2, -1, 0, 1, 1, 2, 3, 4, 5, 6, 10]

test_cases = (-3, -2, -1, 0, 1, 3, 4, 7, 9, 10) 
for number in test_cases:
  index = binary_search(d, number)
  if index != -1:
    print d[index], "==", number, "?", d[index] == number
  else:
    print number, "was not in the list"
--------------------------------------------------------------------

package abc.com.example;

public class BinSearch {
	public static int binSearch(int[] a, int key) {
		int low = 0;
		int high = a.length -1 ;
		while(low <= high) {
			int mid = (low + high) / 2 ;
			if(a[mid] == key) {
				return mid;
			}
			else if(a[mid] > key) {
				high = mid - 1;
			}
			else {
				low = mid + 1;
			}
		}
		return -1;
	}
	
	public static void main(String args[]) {
		int[] a = new int[] {1,3,4,6,8};
		
		System.out.print(BinSearch.binSearch(a, 1));
	
	}
}

