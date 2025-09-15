from typing import Optional, List
from pydantic import BaseModel, ConfigDict

# Step 1: Define a Node
class Node(BaseModel):
    val: int
    next: Optional['Node'] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)  # Allow recursive Node

# Step 2: Define LinkedList
class LinkedList(BaseModel):
    head: Optional[Node] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)  # Allow modifications

    def append(self, val: int) -> None:
        new_node = Node(val=val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self) -> None:
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")



    # Practice: Insert a node at the beginning
    def add_to_beginning(self, val: int) -> None:
        new_node = Node(val=val)
        new_node.next = self.head
        self.head = new_node

    # Practice: Count the number of nodes
    def count_the_nodes(self) -> None:
        curr = self.head
        count = 1
        while curr.next:
            count +=1
            curr.next
            curr = curr.next
        print(count)

    # Practice: Delete a node by value
    def del_node_by_val(self, val:int) -> None:
        curr, prev = self.head, None
    
        while curr.val is not val:
            prev = curr
            curr = curr.next

        if curr.val == val:
            temp = curr
            curr = prev
            curr.next = temp.next
            del temp
        
    # Practice: Reverse the linked list
    def reverse_the_list(self) -> None:
        prev, curr, next = None, self.head, self.head.next

        while curr.next:
            curr.next = prev 
            prev = curr 
            curr = next 
            next = next.next
        curr.next = prev
        self.head = curr
            


        

# ------------------------------------- USAGE ------------------------------------------------
# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.add_to_beginning(1)
ll.count_the_nodes()
ll.display()  # Output: 1 -> 10 -> 20 -> 30 -> 40 -> 50 -> None
ll.del_node_by_val(30)
ll.display() # Output: 1 -> 10 -> 20 -> 40 -> 50 -> None
ll.reverse_the_list()
ll.display() # Output: 50 -> 40 -> 20 -> 10 -> 1 -> None
