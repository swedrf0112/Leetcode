// https://leetcode.com/problems/monotonic-array/
public class isMonotonic{
	
	public static void main(String[] args){
		
		int[] A = {1, 2, 2, 3}; // true
		//int[] A = {1, 3, 0}; // false
		boolean isIncreasing = false;
		boolean isDecreasing = false;
				
		for( int i = 1; i < A.length; i++ ){
			
			if( A[i] - A[i-1] > 0 ){
				
				isIncreasing = true;
				
			}
			
			if( A[i] - A[i-1] < 0 ){
				
				isDecreasing = true;
				
			}
			
		}
		
		System.out.println( isIncreasing & isDecreasing ? false : true );
		
	}
	
}