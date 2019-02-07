## https://leetcode.com/problems/ugly-number/

'''
判斷數值的因數是否只有2, 3, 5, 如果出現其他的因數則return False, ex:
num = 6, return True ( 6 = 2 x 3 )
num = 14, return False ( 14 = 2 x 7 )
'''

## Method 1: Loop
while num > 1:
    if num % 2 == 0:
        num /= 2
    elif num % 3 == 0:
        num /= 3
    elif num % 5 == 0:
        num /= 5
    else:
        return False
        
return num == 1

## Method 2: Recursion
def isUgly(self, num: 'int') -> bool:
    if num == 0: ## 因為0除於任何數字的餘數皆為0, 所以會滿足 num % 2 == 0, num % 3 ==0, num % 5 == 0的條件, 形成死循環
        return False
    elif num % 2 == 0:
        num /= 2
        return self.isUgly(num)
    elif num % 3 == 0:
        num /= 3
        return self.isUgly(num)
    elif num % 5 == 0:
        num /= 5
        return self.isUgly(num)
    else:
        return num == 1