from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.is_empty():
            print('Empty List')
            return
        print('\n---PRINTING LIST---')
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        first_node = self.head
        new_node.next = first_node
        self.head = new_node
    
    def delete_by_value(self, value_to_delete):
        if self.is_empty():
            print('Empty List nothing to delete')
            return
        prev = None
        cur_node = self.head
        
        if cur_node.data == value_to_delete:
            self.head = cur_node.next
            cur_node = None
            return

        while cur_node and cur_node.data != value_to_delete:
            prev = cur_node
            cur_node = cur_node.next
        prev.next = cur_node.next
        cur_node = None
    
    def get_len(self):
        count = 0
        if self.is_empty():
            print(count)
            return
        cur_node = self.head    
        while cur_node:
            count += 1
            cur_node = cur_node.next
        print(f"len = {count}")
        return count

    def delete_by_position(self, position_to_delete):
        if self.is_empty():
            print('Empty list')
            return
        cur_pos = 0
        cur_node = self.head
        if position_to_delete == cur_pos:
            self.head = cur_node.next
            return
        prev = None
        while cur_node and cur_pos != position_to_delete:
            cur_pos += 1
            prev = cur_node
            cur_node = cur_node.next
        prev.next = cur_node.next
        cur_node = None
     
    #TODO: Implement swap nodes   
    def swap_nodes(self, node1, node2):
        pass
    
    #TODO: Implement reverse list method
    def reverse_list(self):
        pass