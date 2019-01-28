## https://leetcode.com/problems/assign-cookies/

'''
找出最多個g中的元素, 使得每一個找出的g, 都可以跟s中的一個元素配成一對, 其中g <= s
g = [1, 2, 3]
     |
s = [1, 1]
output = 1

g = [1, 2]
     |  |
s = [1, 2, 3]
output = 2
'''

'''
Method 1: 暴力法:
(1) 計數s中出現過的元素次數
(2) 排序s中出現過的元素(為了滿足"找出最多個g"這個條件, 先從最小的s開始分)
(3) 遍歷g中所有的元素, 如果發現:
    1. g <= s
	2. 還有s可以分 (s_dict[g] > 0)
	則結果+1, 表示g與這個s配成一對
(4) 把分過的s減去1
'''
s_dict = {}
for i in s:
	if i not in s_dict:
		s_dict[i] = 1
	else:
		s_dict[i] += 1
		
cnt = 0
sort_keys = sorted(s_dict.keys())

for i in g:
	for j in sort_keys:
		if i <= j and s_dict[j] > 0:
			cnt += 1
			s_dict[j] -= 1
			break
			
return cnt


'''
Method 2: 雙指針
先將g與s由小到大排序, 由於排序的關係, 所以可以使用g的指針(g_idx)就可以知道目前已經有幾對符合條件
不符合條件的話就換更大的s, 直到看g跟s誰先遍歷完即可
'''
g.sort()
s.sort()

g_idx, s_idx = 0, 0
while g_idx < len(g) and s_idx < len(s):
	if g[g_idx] <= s[s_idx]:
		g_idx += 1
	s_idx += 1
		
return g_idx