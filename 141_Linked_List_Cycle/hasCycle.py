## https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
給定一個Linked List，確認是否有Cycle? ex:
head = [3, 2, 0, -4], pos = 1
指cycle的index = 1，即 [3, 2, 0, -4 ,2, 0, -4, 2, ...]

比較容易錯的case:
head = [1, 2, 3], pos = -1
head = [], pos = -1
head = [1, 2, 3, 2], pos = -1
'''

'''
Method 1: 用一個HashTable存已經經過的Node，如果發現重複的就確認有Cycle
Time Complexity: O(n), Memory Complexity: O(n)

*是存Node，比較也是比Node物件是否相同，非存Node的value
'''

def hasCycle(self, head: ListNode) -> bool:
    node_dict = {}
    while head:
        if head in node_dict:
            return True
        else:
            node_dict[head] = True
        head = head.next

    return False

'''
Method 2: 用一個快指針(q)、一個慢指針(s)，快指針一次走兩步，慢指針一次走一步，
當快指針指到的Node與慢指針指到的Node相同，表示有Cycle
Time Complexity: O(n), Memory Complexity: O(1)

*如果快指針發現下一步或下兩步是None的話，表示沒有Cycle
'''

def hasCycle(self, head: ListNode) -> bool:
    q = head
    s = head

    while q or s:
        if (q.next is None) or (q.next.next is None):
            return False
        else:
            s = s.next
            q = q.next.next

        if q == s:
            return True
    
    return False