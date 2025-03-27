class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

o1 = LinkedList(100)
print(o1.head.value)



node = {
   'value' : 23,
   'next' : {
    'value' : 4,
    'next' :{
        'value' : 45,
        'next' : {
            'value' : 6,
            'next' :{
                'value': 21,
                'next': None
            }
        }
    }
   } 
}
print(node.keys().mapping)