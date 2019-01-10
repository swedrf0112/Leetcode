## https://leetcode.com/problems/student-attendance-record-i/

'''

'''

## Method 1:
return s.count("A") <= 1 and s.find("LLL") == -1

## 方法二:
a_cnt = 0
l_max_conti_cnt = 0
l_conti_cnt = 0

for i in range(len(s)):
    if s[i] == "L":
        l_conti_cnt += 1
        if i == len(s) - 1 and l_conti_cnt > l_max_conti_cnt:
            l_max_conti_cnt = l_conti_cnt        
    else: 
        if s[i] == "A":
            a_cnt += 1
        
        if l_conti_cnt > l_max_conti_cnt:
            l_max_conti_cnt = l_conti_cnt
            
        l_conti_cnt = 0
		
return a_cnt <= 1 and l_max_conti_cnt <= 2