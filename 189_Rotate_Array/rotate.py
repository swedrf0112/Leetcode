## https://leetcode.com/problems/rotate-array/

'''
input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
output: nums = [5, 6, 7, 1, 2, 3, 4]

題目需要inplace, 進行以下幾個步驟:
(1) 先將前 k 個反轉 => [4, 3, 2, 1, 5, 6, 7]
(2) 再把 k 個之後的反轉 => [4, 3, 2, 1, 7, 6, 5]
(3) 整條序列反轉即可得 => [5, 6, 7, 1, 2 ,3 ,4]
'''

'''
有關於Python使用multiple assignment來swap的詳細說明:
x, y = y, x
Python的計算順序是由右邊先開始, 所以:
(1) y, x 會變成一組tuple
(2) unpacking tuple 後 multiple assignment 到左邊
https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python

跟以下這種寫法是不一樣的:
x = y (x被y所取代)
y = x (y = y)
'''
def reverse_list(nums, start_idx, end_idx):
	while start_idx < end_idx:
		nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
		start_idx += 1
		end_idx -= 1
		
	return nums

if k is None or k <= 0:
	return

k = k % len(nums) ## 避免k值超過nums的長度

nums = reverse_list(nums, 0, len(nums) - k - 1) ## (1) 先將前 k 個反轉 
nums = reverse_list(nums, len(nums) - k, len(nums) - 1) ## (2) 再把 k 個之後的反轉
nums = reverse_list(nums, 0, len(nums) - 1) ## (3) 整條序列反轉