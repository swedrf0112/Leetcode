## https://leetcode.com/problems/two-sum/

'''
找到array中的兩個數字和等於目標數，回傳這兩個數字的index

ex: nums = [2, 7, 11, 15], target = 9
output = [0, 1]
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        O(n): 建立一個map，當掃過整條序列的時候，計算每一個數字跟目標的差值，
              確認是否在map裡，不在的話記在key，index記在value，如果在的話表示差值過去已經出現過了，直接回傳之前的位置即可
        target = 9
        nums = [2]   -> {7:0}
               [7]   -> 發現有在map裡, return [map index, 現在 index]
               [11]
               [15] 
        '''
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target-nums[i]] = i
            else:
                return [d[nums[i]], i]