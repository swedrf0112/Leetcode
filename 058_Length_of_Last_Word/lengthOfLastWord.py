## https://leetcode.com/problems/length-of-last-word/

'''
計算句子中最後一個詞的字串長度
ex: 
"Hello World" => return 5
"aaa bb  " => return 2
'''

## Method 1: Python 內建
return len(s.rstrip().split(" ")[-1)

## Method 2: 從字串由左到右計算, 記住: 
## (1) 最後一次字串的長度
## (2) 最後一個空格的index

s_list = list(s)
s_cnt = 0 ## 
last_space_idx = 0 
last_string_len = 0

for i in range(len(s_list)):
	
	s_cnt += 1

	if i > 0 and s_list[i] == " " and s_list[i-1] != " ": ## 如果遇到空格, 前一格是字的話
		last_string_len = s_cnt - last_space_idx - 1 ## 根據當前字串長度與最後一次空格的index相減, 再 - 1(因為index是從0開始算), 得到最後一次字串的長度

	if s_list[i] == " ": ## 如果遇到空格, 更新最後一次空格的 index
		last_space_idx = s_cnt 

if last_space_idx == s_cnt: ## 如果最後一格空格的index跟字串長度一樣, 表示字串的最後一個字是空格 ex: "a   ", 就回傳最後一個字串的長度
	return last_string_len
else:
	return s_cnt - last_space_idx ## 回傳字串長度 - 最後一個空格的 index 即為最後一個字的長度

