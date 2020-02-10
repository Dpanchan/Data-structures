package com.datastructures.algo;

import java.util.*;


public class QS {
	private static int counter;
	public static void main(String[] args) {
//		var xs = new String[] { "z", "dog", "apple", "ban", "song", "eat", "phone", "queue"};
		var xs = new Integer[] { 4, -3, 2, 1, -90, -10, 10};
		qs(xs);
		System.out.println(Arrays.toString(xs));

		
	}

	private static List<Integer> qs_xs(List<Integer> xs) {
		if (xs.size() > 1) {
			var pivot = xs.get(0);
			var lesser = new ArrayList<Integer>();
			var equals = new ArrayList<Integer>();
			var greater = new ArrayList<Integer>();
			for (var x: xs) {
				(x < pivot   ? lesser :
				(x == pivot) ? equals : 
						           greater).add(x);
			}
			var sorted = qs_xs(lesser);
			sorted.addAll(equals);
			sorted.addAll(qs_xs(greater));
			return sorted;
		}
		return xs;
	}
	
	private static  <T extends Comparable<T>> void qs(T[] xs) {
		qsHelper(xs, 0, xs.length-1);
	}

	private static <T extends Comparable<T>> void qsHelper(T[] a, int i, int j) {
		
		if (i < j) {
			System.out.println("### " + counter++);
			var p = a[i];
//			 5 7 4 5 6 5 1 3
			
//			4 1 3 5 5 5 7 6
			var n = i;
			var k = i;
			while (k <= j) {
				if (a[k].compareTo(p) < 0) {
					var tmp = a[n];
					a[n] = a[k];
					a[k] = tmp;
					n += 1;
				}
				k += 1;
			}
			
			var m = j; 
			k = m;
			while (k >= 0) {
				if (a[k].compareTo(p) > 0) {
					var tmp = a[m];
					a[m] = a[k];
					a[k] = tmp;
					m -= 1;
				}
				k -= 1;
			}
			
			qsHelper(a, i, n-1);
			qsHelper(a, m+1, j);
		}
	}
}
