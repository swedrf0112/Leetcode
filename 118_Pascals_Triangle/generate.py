## https://leetcode.com/problems/pascals-triangle/

'''
計算帕斯卡三角形, 給定層數(numRows), 回傳每一層之數字內容, ex:
numRows = 5
return [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

'''
Method 1: 暴力解, 給定上一層, 照定義計算下一層, 如下: 
outputList[1] = upperList[0] + upperList[1]
outputList[2] = upperList[1] + upperList[2]
...
outputList[i+1] = upperList[i] + upperList[i+1]
'''
def genNumRowList(self, upperList):
        outputList = [1] * (len(upperList) + 1) ## 初始化一個全部為1的序列
        for i in range(len(upperList) - 1): ## 到倒數第二個值
            outputList[i+1] = upperList[i] + upperList[i+1] 
        return outputList
		
if numRows == 0:
	return []
	
output = [[1]]
for i in range(numRows - 1):
    output.append(genNumRowList(output[-1]))

return output

'''
Method 2: 要計算第5層 1 4 6 4 1 時, 把第4層的數字 1 3 3 1 前後各補上0後相加, 即可算出: 
    1 3 3 1 0
  + 0 1 3 3 1
 --------------
    1 4 6 4 1
'''
def getNumRowList(upperList):
    return list(map(lambda x, y: x + y, [0] + upperList, upperList + [0]))
	
if numRows == 0:
	return []
	
output = [[1]]
for i in range(numRows - 1):
    output.append(genNumRowList(output[-1]))

return output