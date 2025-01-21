"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        if head is None:
            return head
    
        curr = head
        newHead = None
        tail = None
    
        while curr is not None:
            groupHead = curr
            prev = None
            nextNode = None
            count = 0
    
            # Reverse the nodes in the current group
            while curr is not None and count < k:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                count += 1
    
            # If newHead is null, set it to the
            # last node of the first group
            if newHead is None:
                newHead = prev
    
            # Connect the previous group to the
            # current reversed group
            if tail is not None:
                tail.next = prev
    
            # Move tail to the end of 
            # the reversed group
            tail = groupHead
    
        return newHead

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends