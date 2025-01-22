#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def reverse(self,head):
        prev = None
        curr = head
        next = None
    
        # Loop to reverse the linked list
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
       # function to trim leading zeros from linked list
    def trimLeadingZeros(self,head):
        while head and head.data == 0:
            head = head.next
        return head
      
    # Recursive function to add two numbers represented
    # by linked lists
    def addListRec(self,num1, num2, carry):
        
        # Base case: If both lists are empty and no carry is left
        if num1 is None and num2 is None and carry[0] == 0:
            return None
    
        sum = carry[0]
    
        # Add the value from the first list if it exists
        if num1 is not None:
            sum += num1.data
            num1 = num1.next
    
        # Add the value from the second list if it exists
        if num2 is not None:
            sum += num2.data
            num2 = num2.next
    
        carry[0] = sum // 10
        result = Node(sum % 10)
    
        # Recursively add remaining digits
        result.next = self.addListRec(num1, num2, carry)
    
        return result
    
    # Function for adding two linked lists
    def addTwoLists(self,num1, num2):
        num1 = self.trimLeadingZeros(num1)
        num2 = self.trimLeadingZeros(num2)
        
        # Reverse both lists to start addition from the 
        # least significant digit
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
    
        carry = [0]
        result = self.addListRec(num1, num2, carry)
    
        # If there's any carry left after the addition,
        # create a new node for it
        if carry[0] != 0:
            newNode = Node(carry[0])
            newNode.next = result
            result = newNode
    
        # Reverse the result list to restore the original order
        return self.reverse(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends