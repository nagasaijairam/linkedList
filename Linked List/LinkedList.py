class Node:
    def __init__(self,val):
        self.val=val
        self.next=None 

# //we are going to learn linked list by urvu goel madam today.        
node1=Node(1)
node2=Node(2)
node1.next=node2

Head=[node1]


def traverse(Head):
    temp=Head[0] 
    while temp !=None:
        print(temp.val,end="->")
        temp=temp.next
    print()

def insertAtHead(x,Head):
    if Head[0]==None:
        insertAtHead(x,Head)
    newHead=Node(x)
    newHead.next=Head[0]
    Head[0]=newHead    


def insertAtEnd(x,Head):
    newNode=Node(x)
    temp=Head[0]
    while temp.next!=None:
        temp=temp.next 
    temp.next=newNode         
             


traverse(Head) #1->2->
insertAtHead(0,Head)#0->1->2->
insertAtEnd(3,Head) #0->1->2->3->
insertAtEnd(4,Head) #0->1->2->3->4->
traverse(Head) #0->1->2->3->4->
