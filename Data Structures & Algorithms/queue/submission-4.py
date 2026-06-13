class Deque:
    
    def __init__(self):
        self.queue = []
        self.length = 0


    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.insert(0,value)
        
    def pop(self) -> int:
        if self.queue:
            return self.queue.pop()
        else:
            return -1
        
    def popleft(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1


        
