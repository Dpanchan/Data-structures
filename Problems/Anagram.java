
public class Anagram {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s1 = "Hello";
		String s2 = "H e l l o";
		s1 = s1.replace(" ","").toLowerCase();
		s2 = s2.replace(" ", "").toLowerCase();
		System.out.println(s1.equals(s2));
	}

}
