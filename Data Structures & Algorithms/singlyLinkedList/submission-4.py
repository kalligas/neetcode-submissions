class LinkedList:
    
    def __init__(self):
        self.linked_list = []
        self.length = 0


    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        return self.linked_list[index]["value"]
        

    def insertHead(self, val: int) -> None:
        next_node = 1 if self.length > 0 else None
        self.linked_list.insert(0,{"next":next_node,"value":val})
        self.length += 1
        

    def insertTail(self, val: int) -> None:
        self.length += 1
        new_tail_position = self.length - 1
        prev_node_position = self.length - 2
        self.linked_list.append({"next":None,"value":val})
        self.linked_list[prev_node_position]["next"] = new_tail_position
        
        

    def remove(self, index: int) -> bool:
        tail_position = self.length - 1
        
        if index > tail_position:
            return False
        
        new_list = []

        for i in range(0,index):
            new_list.append(self.linked_list[i])
        for i in range(index + 1, self.length):
            if self.linked_list[i]["next"]: 
                self.linked_list[i]["next"] -= 1
            new_list.append(self.linked_list[i])
        
        self.length -= 1

        self.linked_list = new_list

        return True
        

    def getValues(self) -> List[int]:
        return [i["value"] for i in self.linked_list]
        
