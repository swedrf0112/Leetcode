// https://leetcode.com/problems/monotonic-array/

public class isMonotonic_v1{
	
	public static void main(String[] args){
		
		int[] A = {1, 2, 2, 3}; // true
		//int[] A = {1, 3, 0}; // false
		
		/*
		(1) 若是單調遞增/單調遞減的序列, 則 isIncreasing/isDecreasing 兩個狀態只會有一個成立
		(2) 相等不考慮
		*/
		
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
		
		// 兩個狀態只會有一個成立, 都成立表示不為單調遞增/單調遞減的序列
		System.out.println( isIncreasing & isDecreasing ? false : true );
		
	}
	
}