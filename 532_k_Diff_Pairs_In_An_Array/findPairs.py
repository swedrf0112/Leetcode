## https://leetcode.com/problems/k-diff-pairs-in-an-array/

'''
於nums數列中兩兩一對, 找出共有多少對唯一的組合, 其中元素相差等於k, ex:
nums = [3, 1, 4, 1, 5], k = 2 
output = 2
共有(1, 3), (3, 5)兩對組合, 相差等於2, 其中(3, 1), (5, 3)已重複, 因此不計,
nums中有兩個1, 所以會有兩對(1, 3), 也只計一對。

nums = [1, 2, 3, 4, 5], k = 1
output = 4
共有 (1, 2), (2, 3), (3, 4), (4, 5)共四對組合

nums = [1, 3, 4, 1, 5], k = 0 
output = 1
僅有(1, 1)這一對組合滿足需求, 
可以發現若 k = 0 為特例, 找出nums中有哪些數字出現超過1次即可, 
如果有數字出現超過2次, 例如[1, 1, 1, 2, 3], 所以配對組合會有 (1, 1), (1, 1), (1, 1)三種配對法
但因為已重複, 所以計算一次即可
'''

from collections import Counter
nums_appear_times = Counter(nums) ## 使用collections.Counter()計算每個nums出現的次數

if k < 0:
	return 0
elif k == 0:
	return len(list(filter(lambda x: x > 1, nums_appear_times.values()))) ##找出nums中有那些數字出現超過1次
else:
    ## 遍歷nums中所有key值, 找出i+k有沒有在nums的key裡面, 有的話即為配對成功
    cnt = 0
    for i in nums_appear_times.keys():
        if i + k in nums_appear_times.keys():
            cnt += 1
			
    return cnt
    #return len(list(filter(lambda x: x + k in nums_appear_times.keys(), nums_appear_times.keys()))) ## 使用filter與上述for loop意義一樣