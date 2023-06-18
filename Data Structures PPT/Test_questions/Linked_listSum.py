"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0] Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]

 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9 It is guaranteed that the list represents a number that does not have leading zeros."""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert(self,data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = newNode
        
def printNodes(head):
    if head==None:
        return head
    curr = head
    while curr:
        print(curr.data,end='->')
        curr=curr.next
    print()
def reverse(head) -> Node:
    if head == None:
        return head
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
        
def add(l1,l2):
    res = []
    carry = 0
    while l1 or l2:
        if l1:
            num1 = l1.data
        else:
            num1=0
        if l2:
            num2 = l2.data
        else:
            num2=0
        digit_sum = num1+num2+carry
        carry = digit_sum//10
        digit_sum = digit_sum%10
        
        res.append(digit_sum)
        l1 =l1.next
        l2 = l2.next
        
    if carry>0:
        res.append(carry)
    return res            
            
l1 = LinkedList()
nums1 = [2,4,3]
for i in nums1:
    l1.insert(i)
    
l2 = LinkedList()
nums2 = [5,6,4]
for i in nums2:
    l2.insert(i)

op1 = reverse(l1.head)
printNodes(op1)

op2 = reverse(l2.head)
printNodes(op2)
res_list = LinkedList()
for i in add(op1,op2):
    res_list.insert(i)
op3 = reverse(res_list.head)
printNodes(op3)