## https://leetcode.com/problems/to-lower-case/

'''
大寫轉小寫, 略過原本字串中有小寫的部分
'''

str = "Hello" ## return hello

## Method 1: 開一個dictionary查表
output_list = []
to_lower_dict = {}
for i in range(ord("A"), ord("Z") + 1):
    to_lower_dict[chr(i)] = chr(i+32)
	
for i in str:
    if i in to_lower_dict:
        output_list.append(to_lower_dict[i])
    else:
        output_list.append(i)
		
return "".join(output_list)

## Method 2: 由於在ascii表中, 英文大小寫是線性轉換 (+32), 直接使用generator轉換, 比Method 1少開dict及list, 速度較快
return "".join(chr(ord(c)+32) if ord("A") <= ord(c) <= ord("Z") else c for c in str)

## Method 3: Python 字串內建lower方法, 應該是最快&方便的方法XD
return str.lower()
