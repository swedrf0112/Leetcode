//https://leetcode.com/problems/buddy-strings/submissions/

class buddyStrings{
	
	public static void main(String[] args){
		
		/*
		(1) 兩個字串如果相等，字串裡面如果有重複的，可以交換位置相等 => return true
		                      字串裡面不重複 => return false
            => 直接開一個 array 紀錄字的出現次數，如果有一個字大於 1 代表可以 swap 之後變成一樣的 ex: aab, aab
			
		(2) 兩個字串如果不相等，紀錄第一個不相等 與 第二個不相等的位置在哪，試試看可不可以 swap 
		*/
		
		//String A = "aaaaaaabc";
		//String B = "aaaaaaacb";
		
		
		String A = "aab";
		String B = "aab";
		
		if ( A.length() != B.length() ){
			
			System.out.println(false); //return false;
		
		}

		char[] A_char_arr = A.toCharArray();
		char[] B_char_arr = B.toCharArray();
		
		
		if ( A.equals(B) ){
			
			int[] counts = new int[26];
			
			for( char c: A_char_arr ){
				
				counts[c - 'a'] += 1;
			
			}
			
			for( int c: counts ){
			
				if ( c > 1 ){
				
					System.out.println(true); // return true;
					
				}
				
			}
			
			System.out.println(false); // return false;
		
		}else{
			
			int first = 0;
			int second = 0;
			
			for( int i = 0; i < A.length(); i++ ){
			
				if ( A.charAt(i) != B.charAt(i) ){
					
					if( first == 0 ){
						
						first = i;
					
					}else if ( second == 0 ){
						
						second = i;
					
					}else{
					
						System.out.println(false); // return false;  超過 2 個不一樣的字 直接return false
						
					}
				
				}
				
			}
			
			if( A_char_arr[first] == B_char_arr[second] && A_char_arr[second] == B_char_arr[first] ){
				
				System.out.println(true); // return true;
			
			}
			
			System.out.println(false); // return false;
			
			
		}
		
	}
	
}	