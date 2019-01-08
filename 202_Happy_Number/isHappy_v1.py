## https://leetcode.com/problems/happy-number/

'''
使用set紀錄出現過的平方和, 如果已在set中, 則不為 Happy Number, return false
'''

n = 19 ## True
total_square = 0
square_num_set = set()

while n != 1:
    while n > 0:  ## 一次加一個位數
        total_square += pow(n % 10, 2)
        n = int(n/10)
    
    if total_square not in square_num_set:
        n = total_square
        total_square = 0
        square_num_set.add(n)
    else:
        return False
else:
    return True