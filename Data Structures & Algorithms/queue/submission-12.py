class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        


class Deque:
    
    def __init__(self):
        self.tail = Node("dummy_tail")
        self.head = Node("dummy_head")
        self.tail.prev = self.head
        self.head.next = self.tail



    def isEmpty(self) -> bool:
        return self.head.next == self.tail and self.tail.prev == self.head

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head.next = new_node
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.tail.prev = new_node
        new_node.prev = self.head
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        my_val = self.tail.prev.value
        self.tail.prev.prev.next=self.tail
        self.tail.prev = self.tail.prev.prev
        return my_val
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        my_val = self.head.next.value
        self.head.next.next.prev=self.head
        self.head.next = self.head.next.next
        return my_val


        
