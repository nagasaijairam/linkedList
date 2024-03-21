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

def insertAtHead(Head,x):
 
    newHead=Node(x)
    newHead.next=Head[0]
    Head[0]=newHead    


def insertAtEnd(Head,x):
    newNode=Node(x)
    temp=Head[0]
    while temp.next!=None:
        temp=temp.next 
    temp.next=newNode         

def insertAtMiddle(Head,x,k):
    if k==1:
        insertAtHead(Head,x)
        return 
    temp = Head[0]
    count=1 
    while  count<k-1:
        temp=temp.next 
        count+=1 
    newNode=Node(x)
    newNode.next=temp.next
    temp.next=newNode

def deleteAtHead(Head):
    if Head[0] is  None:
        return ;
    temp=Head[0] 
    Head[0]=temp.next 

def deletAtLast(Head):
    if Head[0] == None:
        return 
    if Head[0].next==None:
        deleteAtHead(Head)
    temp=Head[0]
    while temp.next.next!=None:
        temp=temp.next 

    temp.next=None   


             


# traverse(Head) #1->2->
insertAtHead(Head,0)#0->1->2->
insertAtEnd(Head,3) #0->1->2->3->
# insertAtEnd(Head,4) #0->1->2->3->4->
# insertAtMiddle(Head,1.5,3)
# deleteAtHead(Head)
# traverse(Head) #0->1->2->3->4->
