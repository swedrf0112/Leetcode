## https://leetcode.com/problems/can-place-flowers/

'''
給定花的數量(n), 以及目前花圃上的狀況(flowerbed), 回傳可不可以種下n朵花, 其中兩朵花之間不能相鄰
ex:
[1, 1, 0], n = 1    ===> False
[1, 0, 0, 0, 1], n = 2 ===> False ## 種不下2朵不相鄰的花
[1, 0, 0, 0, 1], n = 1 ===> True ## 可以把1朵花中在第三個位置

使用貪心算法, 從左到右掃一遍, 只要能種就種下去
'''

flowerbed = [1, 0, 0, 0, 1]
n = 2

if len(flowerbed) == 1 and flowerbed[0] == 0: ## 考慮 flowerbed = [0] & n = 1 的情況
    return n <= 1

for i in range(len(flowerbed)):
    if flowerbed[i] == 0:        
        if i == 0: ## 考慮最左邊的邊界, 只要右邊那1格是0就可以
            if flowerbed[i+1] == 0: 
                flowerbed[i] = 1
                n -= 1
                
        elif i == (len(flowerbed) - 1): ## 考慮最右邊的邊界, 只要左邊那1格是0就可以
            if flowerbed[i-1] == 0: 
                flowerbed[i] = 1
                n -= 1     
			
        else:
            if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
                
        if n < 0: ## 如果已經沒有花可以插了, return True
            return True
        
return n == 0