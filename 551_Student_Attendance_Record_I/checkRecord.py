## https://leetcode.com/problems/student-attendance-record-i/

'''
給定一字串s, 其中如果"A"大於2個, 或連續2個以上都是"L"的話 return False
'''

## Method 1: 使用 Python 內建函數
return s.count("A") <= 1 and s.find("LLL") == -1

## Method 2: 從頭開始掃, 滿足條件即報 False
a_cnt = 0
l_conti_cnt = 0

for i in range(len(s)):
    if s[i] == "L":
        l_conti_cnt += 1
        if l_conti_cnt > 2:
        return False

    else: 
        l_conti_cnt = 0 ## 如果字是"A"或"P", 連續的L count歸0
        if s[i] == "A":
            a_cnt += 1
            if a_cnt > 2:
                return False

return True