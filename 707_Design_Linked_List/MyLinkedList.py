## https://leetcode.com/problems/design-linked-list/

'''
建立一個Linked List, 包含 get, addAtHead, addAtTail, addAtIndex, deleteAtIndex等方法
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
			
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size: ## 最後一個可以access的Node是self.size-1
            return -1
        
        if self.head is None: ## 如果串列沒有頭
            return -1
        
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        
        return ptr.val
        
    
    def addAtHead(self, val):
        self.addAtIndex(0, val) ## 透過addAtIndex方法
    
    def addAtTail(self, val):
        self.addAtIndex(self.size, val) ## 透過addAtIndex方法
    
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        
        if index < 0 or index > self.size: ## 如果index小於0, 或者index比長度還長(***最後一個可以加入Node的index是self.size!!)
            return
        
        '''
        分三種情形:
        (1) Node加在串列最前端: 把self.head換掉
        (2) Node加在串列之中: 用ptr移動到index的前一格, 把新的Node接在原本index的前面, 再把index前一格的後面接上新Node
        (3) Node加在串列最尾端: 原本index就是None, 所以就可以跟(2)寫在一起
        '''
        newnode = Node(val)
        if index == 0:
            newnode.next = self.head ## 把self.head放在新Node的後面
            self.head = newnode ## 把self.head換掉
        else:
            ptr = self.head
            for i in range(index - 1):
                ptr = ptr.next
            
            newnode.next = ptr.next ## 把新的Node接在原本index的前面
            ptr.next = newnode ## 把index前一格的後面接上新Node
    
        self.size += 1
    
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        
        if index < 0 or index >= self.size: ## 最後一個能刪的index是self.size - 1
            return 
        
        '''
        分三種情形:
        (1) 刪掉最前端的Node: 把head換成head的下一個, 已經刪完的話會因為ptr.next = None而指向None
        (2) 刪掉中間的Node: 用ptr移動到要刪的index前一格, 把原本的ptr.next指向ptr.next.next(跳過一個Node)
        (3) 刪掉最尾端的Node: 同(2) ptr.next是最後一格, ptr.next.next已經是None, 所以直接把ptr.next指向ptr.next.next即可
        '''
        
        ptr = self.head
        if index == 0:
            self.head = ptr.next
        else:
            for i in range(index - 1):
                ptr = ptr.next
                
            ptr.next = ptr.next.next
        
        self.size -= 1
        
    
    def print(self):
        ptr = self.head
        while ptr != None:
            print("[%d]" % ptr.val, end = "")            
            ptr = ptr.next
    