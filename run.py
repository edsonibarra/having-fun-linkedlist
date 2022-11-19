from linkedlist import LinkedList


def main():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.get_len()
    ll.print_list()

    ll.prepend(0)

    ll.print_list()

    ll.delete_by_value(2)

    ll.print_list()

    ll.delete_by_value(0)
    
    ll.print_list()
    
    ll.delete_by_value(1)
    
    ll.print_list()
    
    ll.get_len()
    
    ll.delete_by_position(1)
    
    ll.print_list()
    ll.get_len()  
    
    ll.delete_by_position(0)
    
    ll.print_list()
    ll.get_len()  

main()  
