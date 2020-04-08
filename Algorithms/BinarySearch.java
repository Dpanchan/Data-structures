package com.datastructures.algo;

import java.util.Arrays;

public class BinarySearch {

	public static void main(String[] args) {
		Long[] arr = { 4L, 5L, 6L, 7L, 8L, 9L };
		Long key = 8L;
		String[] fruits = {"banana", "apple", "orange", "pear"};
		Arrays.sort(fruits);
		String fruit = "pine apple";
		
		int pos = binarySearch(fruits, fruit);
		if (pos != -1) {
			System.out.println("Found the key " + fruit + " at position: " + pos);
		} else {
			System.out.println("Key not found in the given array");
		}
	}

	public static <T extends Comparable<T>> int binarySearch(T[] arr, T key) {
		int low = 0, high = arr.length - 1;
		while (low <= high) {
			int mid = (low + high) / 2;
			if (arr[mid] == key) {
				return mid;
			} else if (arr[mid].compareTo(key) > 0) {
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		return -1;
	}
}
