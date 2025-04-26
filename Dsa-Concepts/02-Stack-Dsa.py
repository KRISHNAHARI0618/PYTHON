# Defining The Class

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def stack_push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height = self.height+1

stacklist = Stack(10)
stacklist.print_stack()

print("Stack Push Is Started")
stacklist.stack_push(20)
stacklist.stack_push(30)
stacklist.print_stack()