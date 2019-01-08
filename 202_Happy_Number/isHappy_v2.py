## https://leetcode.com/problems/happy-number/

'''
使用set紀錄出現過的平方和, 如果已在set中, 則不為 Happy Number, return false
'''

n = 19 ## True
total_square = 0

square_num_set = set()
while n != 1:
    n = sum(int(i) ** 2 for i in str(n)) #將int轉成str後, 使用 generator將一格格的character累加
    if n in square_num_set:
        return False
    else:
        square_num_set.add(n)
else:
    return True