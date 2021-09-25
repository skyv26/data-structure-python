import copy

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.list_size = 0

    def addNode(self, val):
        type_str = type(val).__name__
        checker = (type_str == 'str' or type_str == 'int')
        if(self.head is None):
            if(checker):
                val = str(val)
                self.head = Node(val)
                self.list_size += 1
            else:
                self.head = Node(val[0])
                self.list_size += 1
                self.addNode(val[1:])

        else:
            itr = self.head
            if(not checker):
                for each in val:
                    each = str(each)
                    self.addNode(each)
            else:
                while(itr.next is not None):
                    itr = itr.next
                itr.next = Node(val)
                self.list_size += 1

    def deleteNode(self, val):
        checker = str(type(val).__name__)
        checker = (checker == 'str' or checker == 'int')
        itr=self.head
        if(checker):
            if(str(itr.data) == str(val)):
                self.head = itr.next
                itr=None
                self.list_size-=1
            else:
                while itr:
                    if(str(itr.data) == str(val)):
                        break
                    prev = itr
                    itr=itr.next
            
            if(itr is not None):
                prev.next=itr.next
                self.list_size-=1
        else:
            for each in val:
                self.deleteNode(str(each))

    def display(self, itr=''):
        out_str = ''
        if(len(itr) < 1):
            itr = self.head
        while itr:
            out_str += str(itr.data)+' => '
            itr = itr.next
        out_str += "NULL"
        print('\n', out_str+" ,", "size:", self.list_size, '\n')


list = LinkedList()
list.addNode([a for a in range(20)])
list.display()
list.deleteNode([a for a in range(20) if a%2==0])
list.display()
print()
