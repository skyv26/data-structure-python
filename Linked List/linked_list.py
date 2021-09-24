from copy import copy

class Node:
    def __init__(self,data=None, next_node=None):
        self.data=data
        self.next=next_node

class LinkedList:
    def __init__(self):
        self.head=None
        self.list_size=0
    
    def addNode(self,val):
        type_str=str(type(val)).replace('>','').replace('<','').replace("'",'').split(' ')[1]
        checker=(type_str == 'str' or type_str == 'int')
        if(self.head is None):
            if(checker):
                val=str(val)
                self.head=Node(val)
                self.list_size+=1
            else:
                oneTime=True
                for each in val:
                    each=str(each)
                    if(oneTime):
                        firstNode=Node(each)
                    else:
                        firstNode.next=Node(each)
                self.head=firstNode
        else:
            itr=self.head
            if(not checker):
                for each in val:
                    each=str(each)
                    self.addNode(each)
            else:
                while(itr.next is not None):
                    itr=itr.next
                itr.next=Node(val)
                self.list_size+=1

    def display(self):
        out_str=''
        itr=self.head
        while itr:
            out_str+=str(itr.data)+' => '
            itr=itr.next
        out_str+="NULL"
        print('\n',out_str+" ,", "size:",self.list_size,'\n')

list=LinkedList()
list.addNode(5)
list.addNode([10,15,20,25,7])
list.addNode(55)



list.display()