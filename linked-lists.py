from typing import Optional, List
from pydantic import BaseModel, ConfigDict

# Step 1: Define a Node
class Node(BaseModel):
    val: int
    nxt: Optional['Node'] = None

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
        while current.nxt:
            current = current.nxt
        current.nxt = new_node

    def display(self) -> None:
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.nxt
        print("None")



    # Practice: Insert a node at the beginning
    def add_to_beginning(self, val: int) -> None:
        new_node = Node(val=val)
        new_node.nxt = self.head
        self.head = new_node

    # Practice: Count the number of nodes
    def count_the_nodes(self) -> None:
        curr = self.head
        count = 1
        while curr.nxt:
            count +=1
            curr.nxt
            curr = curr.nxt
        print(count)

    # Practice: Delete a node by value
    def del_node_by_val(self, val:int) -> None:
        curr, prev = self.head, None
    
        while curr.val is not val:
            prev = curr
            curr = curr.nxt

        if curr.val == val:
            temp = curr
            curr = prev
            curr.nxt = temp.nxt
            del temp
        
    # Practice: Reverse the linked list
    def reverse_the_list(self) -> None:
        prev, curr, nxt = None, self.head, self.head.nxt

        while curr.nxt:
            curr.nxt = prev 
            prev = curr 
            curr = nxt 
            nxt = nxt.nxt
        curr.nxt = prev
        self.head = curr
            
    # Practice: Merge two sorted linked lists
    def merge_two_lits(self, list_a: Node, list_b: Node) -> Node:
        curr = None
        starting_node = None

        while list_a.nxt and list_b.nxt:
            if list_a.val > list_b.val:
                curr = list_b
                list_b = list_b.nxt
                if curr.nxt.val > list_a.val: # only reassign .nxt if the current .nxt is bigger than the current list_a node
                    curr.nxt = list_a 
            else:
                curr = list_a
                list_a = list_a.nxt
                if curr.nxt.val > list_b.val:# only reassign .nxt if the current .nxt is bigger than the current list_b node
                    curr.nxt = list_b 

            if starting_node == None:
                starting_node = curr

            curr = curr.nxt
        self.head = starting_node


# ------------------------------------- USAGE ------------------------------------------------
# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
second_ll = LinkedList()
second_ll.append(2)
second_ll.append(11)
second_ll.append(22)
second_ll.append(33)
second_ll.append(44)
second_ll.append(55)
ll.add_to_beginning(1)
ll.count_the_nodes()
ll.display()  # Output: 1 -> 10 -> 20 -> 30 -> 40 -> 50 -> None
ll.del_node_by_val(30)
ll.display() # Output: 1 -> 10 -> 20 -> 40 -> 50 -> None
# ll.reverse_the_list()
# ll.display() # Output: 50 -> 40 -> 20 -> 10 -> 1 -> None
ll.merge_two_lits(ll.head, second_ll.head)
ll.display() # Output: 1 -> 2 -> 10 -> 11 -> 20 -> 22 -> 40 -> 44 -> 55 -> None