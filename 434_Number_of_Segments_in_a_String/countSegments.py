## https://leetcode.com/problems/number-of-segments-in-a-string/

'''
將字串根據空格切開, 計算共有幾個字
'''

## 不使用 s.split(" ")
s = "Hello, my name is John" ## return 5
cnt = 0
for i in range(len(s)):
    if i == len(s) - 1 and s[i] != " ": ## 最後一格是字的話 => cnt + 1
        cnt += 1
        
    if i > 0 and s[i-1] != " " and s[i] == " ": ## "a " <- 對應前面有字 後面是空格 標準的分隔 => cnt + 1
        cnt += 1
		
return cnt 

## 使用 s.split(" ")
return len(list(filter(lambda x: x != "", s.split(" "))))
		
		