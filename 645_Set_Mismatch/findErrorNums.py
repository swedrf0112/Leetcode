## https://leetcode.com/problems/set-mismatch/

'''
[1, 2, 2, 4] => 要找出重複值跟缺失值 [2, 3]

先做出參考應該要有的數字 {1, 2, 3, 4}
缺失值 sum([1, 2, 3, 4]) - sum(set([1, 2, 2, 4])) => 3
重複值 sum([1, 2, 2, 4]) - sum(set([1, 2, 2, 4])) => 2
'''

nums = [1, 2, 2, 4]
sum_all = sum(range(1, len(nums)+1))
sum_nums = sum(nums)
sum_nums_set = sum(set(nums))

missing = sum_all - sum_nums_set
duplicate = sum_nums - sum_nums_set

[duplicate, missing]