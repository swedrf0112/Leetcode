## https://leetcode.com/problems/first-bad-version/

'''
題目中有給一個isBadVersion(version)的API, 把integer的版本號丟進去會回傳boolean的結果,
例如第一個傳回True的版號是9, 所以測試的範例函數可以這樣寫:
def isBadVersion(version):
    return version >= 9

題目希望用最快的方法找出第一個Bad(傳回True)的Version, 以上一個範例而言就是9
'''

'''
使用Binary Search實作, 因為序列是一個已經排序好的序列(照版號搜尋), worst time complexity O(log n)

[False, False, True], start = 1, mid = 2, end = 3
isBadVersion(2) == False: start = mid + 1 = 3

[False, False, True], start = 3, mid = 2, end = 3
==> stop loop, return start 即為第一個Bad的版本
'''

start, end = 1, n ## n為題目中的argument
while start <= end:
    mid = (start + end) // 2
    if isBadVersion(mid): ## 如果發現是Bad Version(True), 表示第一個Bad的版本會在mid的前面
        end = mid - 1 ## 把 end 換成 mid - 1
    else: ## 如果發現是Good Version(False), 表示第一個Bad的版本會在mid的後面
        start = mid + 1 ## 把 start 換成 mid + 1
return start
