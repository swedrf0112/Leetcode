## https://leetcode.com/problems/reverse-vowels-of-a-string/

'''
反轉字串中的母音 ex: 
hello => holle
axecdigobu => uxocdigeba (原本字串內的母音出現順序為 aeiou, 反轉成 uoiea)
'''

## Method 1 暴力解, 把出現母音的地方換成空值, 出現過的母音記錄到 s_list 中, 再 pop 填回去
s_list = list(s)
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} ## 使用set可以增加查詢速度

vowel_list = []
for i in range(len(s_list)):
    if s_list[i] in vowels:
        vowel_list.append(s_list[i])  ## 紀錄出現的母音
        s_list[i] = ""  ## 填上空值
		
for i in range(len(s_list)):
    if s_list[i] == "":
        s_list[i] = vowel_list.pop() ## 把紀錄母音的list pop出來(即反轉)
		
return "".join(s_list)

## Method 2 使用雙指針

## Method 3 使用 regular expression