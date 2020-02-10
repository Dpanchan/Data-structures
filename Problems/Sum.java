import java.util.HashSet;
import java.util.Set;

public class Sum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] arr = {5,5,7,8,2,3,2};
		int targetsum = 10;
		Set<Integer> s = new HashSet<>();
		for(int a: arr) {
			int wanted = targetsum - a;
			if(s.contains(wanted)) {
				System.out.println(wanted + " " + a);
				s.remove(wanted);
			} else {
				s.add(a);
			}
		}
		System.out.println("done");
	}

}
