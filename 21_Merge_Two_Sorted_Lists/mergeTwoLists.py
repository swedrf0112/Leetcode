## https://leetcode.com/problems/merge-two-sorted-lists/

'''
把兩個ListNode組成的sorted List, 根據由小到大的順序合併成一個ListNode
l1: 1 -> 2 -> 4
l2: 1 -> 3 -> 4

output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

因為不是LinkedList, 先建立頭尾兩個指針, 
tailNode用來新增節點，最後會指向最後一個ListNode
headNode會一直指向第一個ListNode, 最後return
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

tailNode = headNode = ListNode(None) ## 初始化 tailNode, headNode 兩個指針
        
while l1 and l2: ## 使用 l1 != None and l2 != None 會比較慢...
	'''
	不需要相等的原因如下:
	step 1: l1 = 1, l2 = 1
	        l1.val <= l2.val, tailNode.next = l1, l1 = l1.next -----> [1]
	step 2: l1 = 2, l2 = 1
	        l2.val > l2.val, tailNode.next = l2, l2 = l2.next  -----> [1][1]
	step 3: l1 = 2, l2 = 3
	        l1.val <= l2.val, tailNode.next = l1, l1 = l1.next -----> [1][1][2]
	所以遇到相等的情況，l1會先加進去, 第二步的時候, l1就會大於l2, 把l2一起加進去, 所以不須額外寫相等的情況
	'''
    if l1.val <= l2.val: 
        tailNode.next = l1
        l1 = l1.next
    else:
        tailNode.next = l2
        l2 = l2.next
                
    tailNode = tailNode.next ## 移動tailNode指針到下一格
        
'''
到最後如果 l1 已經到底了, 但l2還有東西, 把l2的東西全部放到tailNode的後面去(因為l2已經預排序完了), 反之亦然
if l1 == None:
    tailNode.next = l2
        
if l2 == None:
    tailNode.next = l1
'''
        
tailNode.next = l1 or l2 ## 與上面的寫法一致
        
return headNode.next