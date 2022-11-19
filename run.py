from linkedlist import LinkedList


def main():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.print_list()

    ll.prepend(0)

    ll.print_list()

    ll.delete_by_value(2)

    ll.print_list()

    

main()  
