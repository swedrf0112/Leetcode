## https://leetcode.com/problems/valid-palindrome/

'''
將字串變成小寫及去掉符號後, 檢查從左到右跟從右到左的字串長的是否一樣(是否回文), ex:
s = "A man, a plan, a canal: Panama" ==> return True
s = "race a car" ==> return False
s = "" ==> return True

如果可以回文的字串, 會發現字串是對稱的, 所以只要比前面一半, 跟倒過來後面一半是不是一樣就好, 這樣可以省去一半的掃描list時間 ex:
s = "aabbaa" ==> 只需要比前面3個字(index: 0, 1, 2) 跟後面3個字(index: 3, 4, 5) 是一樣的即可
s = "aabaa" ==> 奇數個, 中間的b不影響回文
'''

## Method 1: Slice list
if s == "":
	return True
	
s = "".join([i for i in s if i.isalnum()]).lower() ## 使用isalnum方法可以只取數字符號

return s[:int(len(s)/2)] == s[int((len(s) + 1)/2:][::-1] ## 比較前半段(到 int(len(s))/2), 與後半段從 int(len(s)+1)/2 開始的字串


## Method 2: Using two index
if s == "":
	return True
	
s = "".join([i for i in s if i.isalnum()]).lower() ## 使用isalnum方法可以只取數字符號

head_ind = 0 ## 頭部指針
tail_ind = len(s)-1 ## 尾部指針
       
while head_ind < tail_ind: ## 如果頭部指針 >= 尾部指針, 表示已經掃超過字串的一半了
    if s[head_ind] != s[tail_ind]:
        return False
           
    head_ind += 1
    tail_ind -= 1
            
return True

## Method 3: Using map/filter/reversed lazy evaluation, in-place 方法
if s == "":
	return True
	
head_to_tail = map(str.lower, filter(str.isalnum, s)) 
tail_to_head = map(str.lower, filter(str.isalnum, reversed(s)))

return all(x == y for x, y in zip(head_to_tail, tail_to_head)) ## 在all()才實際進行iterate, 所以不用跟前兩個方法一樣要做兩個iterate(先取完數字符號再掃描), 但缺點是不知道怎麼只掃一半XD


