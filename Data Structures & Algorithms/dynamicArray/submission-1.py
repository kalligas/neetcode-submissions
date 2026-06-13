class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dynamic_array = [0] * capacity


    def get(self, i: int) -> int:
        return self.dynamic_array[i]

    def set(self, i: int, n: int) -> None:
        self.dynamic_array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        self.dynamic_array[self.size] = n
        self.size = self.size + 1

    def popback(self) -> int:
        self.size = self.size - 1
        return self.dynamic_array[self.size]
 

    def resize(self) -> None:
        self.dynamic_array = self.dynamic_array + [0] * self.capacity
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity