## https://leetcode.com/problems/search-insert-position/

'''
將target數字插入到已排序好的序列中, 返回可插入的index
若序列中含有target, 則返回target的index
ex:
nums = [1,3,5,6], target = 5, return 2 (找到)
nums = [1,3,5,6], target = 2, return 1 (沒找到, 插入在1的位置)
nums = [1,3,5,6], target = 7, return 4 (沒找到, 大於最後一個值, 插入最後一個位置)
nums = [1,3,5,6], target = 0, return 0 (沒找到, 小於第一個值, 插入第一個位置)
'''

## Method 1: Using loop, time complexity O(N)
if target < nums[0]: ## 小於第一個值, return 第一個位置
    return 0
elif target > nums[-1]: ## 大於最後一個值, return 最後一個位置
    return len(nums)
else:
    for i in range(len(nums)):
        if nums[i] == target or (i > 0 and target > nums[i-1] and target < nums[i]): ## 如果找到, 或是在 (nums[i-1], nums[i]) 之間, return 第i個位置
            return i

## Method 2: Using binary search, time complexity O(log(N))
## 使用 Binary Search, 若找到即回傳
l = 0
r = len(nums) - 1

while l <= r:
    m = (l + r) // 2
        
    if target < nums[m]:
        r = m - 1
    elif target > nums[m]:
        l = m + 1
    else:
        return m
        
return l
'''
沒找到分3種情況:
(1) target 是最大的, l=r=m=len(nums) 後會觸發 l=m+1, 所以回傳l就是最後一個位置
(2) target 是最小的, l=r=m=0 後會觸發 r=m-1, 使得 l > r, 所以回傳l就是第一個位置
(3) target 在序列中間, 回傳l即可
'''
			
