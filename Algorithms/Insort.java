package com.datastructures.algo;

public class Insort {

	public static void main(String[] args) {
		Long[] arr = { 4L, 15L, 16L, 18L, 19L };
		Long key = 1L;
//		String[] fruits = {"banana", "apple", "orange", "pear"};
//		Arrays.sort(fruits);
//		String fruit = "pine apple";

		System.out.println("You can place the key " + key + " at position: " + binarySearch(arr, key));

	}

	public static <T extends Comparable<T>> int binarySearch(T[] arr, T key) {
		int low = 0, high = arr.length - 1;
		int mid = 0;
		while (low <= high) {
			mid = (low + high) / 2;
			if (arr[mid] == key) {
				break;
			} else if (arr[mid].compareTo(key) > 0) {
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		return (mid == high) ? mid + 1 : mid;
	}
}
