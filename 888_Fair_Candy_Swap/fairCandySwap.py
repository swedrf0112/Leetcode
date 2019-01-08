## https://leetcode.com/problems/fair-candy-swap/

# A = [1, 2, 5]
# B = [2, 4]
# return [5, 4]

'''
A跟B交換一個數字, 使得 sum(A) == sum(B)

從暴力解知道:
for i in range(len(A)):
	for j in range(len(B)):
		if sum(B) - B[j] + A[i] == sum(A) - A[i] + B[j]:
			return [A[i], B[j]]
			
化簡 sum(B) - B[j] + A[i] == sum(A) - A[i] + B[j]
=> 2A[i] - 2B[j] = sum(A) - sum(B)
=> B[j] = A[i] - (sum(A) - sum(B)) / 2

所以, 只要遍歷A, 找出計算完的結果有沒有出現在B中即可
'''

sum_a, sum_b, set_b = sum(A), sum(B), set(B)
diff = (sum_a - sub_b)/2

for val in A:
	target = int(val - diff)
	if target in set_b:
		return [val, target]

	