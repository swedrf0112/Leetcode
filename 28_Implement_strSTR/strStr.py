## https://leetcode.com/problems/implement-strstr/

'''
找出haystack字串中符合needle字串的子字串, 回傳其位置, ex:
haystack = "hello"
needle = "ll"
output = 2

haystack = "aaaaa"
needle = "bba"
output = -1
'''

## Method 1: Slice list by window, Time Complexity: O(haystack_len * needle_len)
haystack_len = len(haystack)
needle_len = len(needle)

if needle_len > haystack_len: ## 如果needle的字串長度大於haystack, needle一定不是haystack的子字串
	return -1

'''
以下這兩種例外狀況是需要回傳位置0的:
(1) haystack = "" and needle = ""   ---> needle_len == 0 and haystack_len == 0
(2) haystack = "a" and needle = ""  ---> needle_len == 0 and haystack_len > 0
'''
if needle_len == 0 and haystack_len >= 0:
	return 0

for i in range(haystack_len - needle_len + 1): ## 最後一個scan的位置在 haystack_len - needle_len
	
	if haystack[i] != needle[0]: ## 如果開頭第一個字就不一樣, 就不用比了, 直接跳過
		continue
	
	if haystack[i:(i + needle_len)] == needle: ## Window包起來的字一樣的話, return位置i
		return i
	
return -1

## Method 2: Knuth-Morris-Pratt Algorithm, Time Complexity O(log(needle_len))

