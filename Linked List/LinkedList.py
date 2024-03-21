class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Initialize the linked list with a single node
Head = Node(1)

# Function to traverse and print the linked list
def traverse(Head):
    temp = Head
    while temp != None:
        print(temp.val, end="->")
        temp = temp.next
    print()

# Function to insert a new node at the beginning of the linked list
def insertAtHead(Head, x):
    newHead = Node(x)
    newHead.next = Head
    Head = newHead
    return Head

# Function to insert a new node at the end of the linked list
def insertAtEnd(Head, x):
    newNode = Node(x)
    if Head is None:
        return newNode
    temp = Head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return Head

# Function to insert a new node at a specified position in the linked list
def insertAtMiddle(Head, x, k):
    if k == 1:
        return insertAtHead(Head, x)
    temp = Head
    count = 1
    while count < k - 1 and temp != None:
        temp = temp.next
        count += 1
    if temp == None:
        print("Position out of range")
        return Head
    newNode = Node(x)
    newNode.next = temp.next
    temp.next = newNode
    return Head

# Function to delete the first node of the linked list
def deleteAtHead(Head):
    if Head is None:
        return None
    Head = Head.next
    return Head

# Function to delete the last node of the linked list
def deleteAtLast(Head):
    if Head is None:
        return None
    if Head.next is None:
        return None
    temp = Head
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return Head


# Example usage:
traverse(Head) # Output: 1->
Head = insertAtHead(Head, 0)
traverse(Head) # Output: 0->1->
Head = insertAtEnd(Head, 3)
traverse(Head) # Output: 0->1->3->
Head = insertAtMiddle(Head, 1.5, 3)
traverse(Head) # Output: 0->1->1.5->3->
Head = deleteAtHead(Head)
traverse(Head) # Output: 1->1.5->3->
Head = deleteAtLast(Head)
traverse(Head) # Output: 1->1.5->


             


# traverse(Head) #1->2->
insertAtHead(Head,0)#0->1->2->
insertAtEnd(Head,3) #0->1->2->3->
# insertAtEnd(Head,4) #0->1->2->3->4->
# insertAtMiddle(Head,1.5,3)
# deleteAtHead(Head)
# traverse(Head) #0->1->2->3->4->
