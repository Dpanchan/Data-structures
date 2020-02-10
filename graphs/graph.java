package com.datastructures;

import java.sql.Array;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Graph {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int v = 5;
		int[][] edges = new int[][] { { 0, 1 }, { 1, 2 }, { 2, 3 }, { 0, 4 } };
		int[][] arr = new int[v][v];

		for (int[] edge : edges) {
			int u = edge[0];
			int w = edge[1];
			arr[u][w] = 1;
			arr[w][u] = 1;

		}

		for (int[] edge : arr) {
			System.out.println(Arrays.toString(edge));
		}

		List<List<Integer>> adjList = new ArrayList<>();
		
		for(int i = 0; i < v; i++)
			adjList.add(new ArrayList<>());
		
		System.out.println(adjList);
		
		for(int[] edge: edges) {
			int u = edge[0], v0 = edge[1];
			adjList.get(u).add(v0);
			adjList.get(v0).add(u);
		}
		
		for(int i = 0; i < v; i++) {
			System.out.println(i + " " + adjList.get(i));
		}
		
	
	}
}
