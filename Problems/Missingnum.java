
public class Missingnum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a1 = {1,2,3,5,35};
		int[] a2 = {2,5,3,35};
		int tmp = 0;
		for(int a: a1) {
			tmp ^=a ;
		}
		for(int a: a2) {
			tmp ^= a ;
		}
		System.out.println(tmp);
	}

}
