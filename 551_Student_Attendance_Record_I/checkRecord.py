## https://leetcode.com/problems/student-attendance-record-i/

a_cnt = 0
l_max_conti_cnt = 0
l_conti_cnt = 0
for i in range(len(s)):
    if s[i] == "L":
        l_conti_cnt += 1
    else: 
        if s[i] == "A":
            a_cnt += 1
        
        if l_conti_cnt > l_max_conti_cnt:
            l_max_conti_cnt = l_conti_cnt
            
        l_conti_cnt = 0
        
if l_conti_cnt > l_max_conti_cnt:
    l_max_conti_cnt = l_conti_cnt
		
return a_cnt <= 1 and l_max_conti_cnt <= 2