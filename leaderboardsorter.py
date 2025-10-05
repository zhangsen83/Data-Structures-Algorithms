# Node class for singly linked list
class Node:
    def __init__(self,data,name):
        self.data = data   # numeric value (score)
        self.name = name   # name (player name)
        self.next = None   # pointer to next node

# Linked List class with QuickSort implementation
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a node at the end
    def insert_end(self,data,name):
        new_node = Node(data,name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Utility to convert linked list to array for printing
    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append((current.data,current.name))
            current = current.next
        return result

    # Utility to get the tail of the list
    def get_tail(self, node):
        while node and node.next:
            node = node.next
        return node

    # Partition function similar in structure to array version
    def partition(self, head, end, ascend = True, sorted_by = "data"):
        pivot = end
        prev = None
        curr = head
        tail = pivot
        new_head = None

        # Traverse through list and rearrange nodes
        while curr != pivot:
            next_node = curr.next

            # Compare current node with pivot based on sort type (data or name) and order (ascend or descend)
            if sorted_by == "data":
                if ascend:
                    in_order = curr.data <= pivot.data
                else: #descend
                    in_order = curr.data >= pivot.data
            
            # sorted_by == "name"
            else:
                if ascend:
                    in_order = curr.name.lower() <= pivot.name.lower()
                else: #descend
                    in_order = curr.name.lower() >= pivot.name.lower()

            if in_order:
                # Add node to the left partition
                if new_head is None:
                    new_head = curr
                prev = curr
            else:
                # Move node to the right partition
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                curr.next = None
                tail.next = curr
                tail = curr
            curr = next_node

        if new_head is None:
            new_head = pivot

        return new_head, pivot, tail

    # Recursive quick sort function
    def quick_sort_rec(self, head, end, ascend = True, sorted_by = "data"):
        if head is None or head == end:
            return head

        new_head, pivot, new_end = self.partition(head, end, ascend, sorted_by)

        # Sort left part before pivot
        if new_head != pivot:
            temp = new_head
            while temp.next != pivot:
                temp = temp.next
            temp.next = None

            new_head = self.quick_sort_rec(new_head, temp, ascend, sorted_by)

            tail = self.get_tail(new_head)
            tail.next = pivot

        # Sort right part after pivot
        pivot.next = self.quick_sort_rec(pivot.next, new_end, ascend, sorted_by)

        return new_head

    # Public function to start QuickSort
    def quick_sort(self, ascend=True, sorted_by = "data"):
        self.head = self.quick_sort_rec(self.head, self.get_tail(self.head), ascend, sorted_by)

# Main program
if __name__ == "__main__":
    print("Quick Sort (Linked List Version - Player Leaderboard Sorter)")

    # Ask user for number of people
    while True:
        try:
            nop = int(input("Please Enter Number Of People (eg. 9): "))
            if nop > 0:
                break
            else:
                print("Invalid Input. Please Enter A Number Greater Than 0!")

        except ValueError:
            print("Invalid Input. Please Enter A Number!")

    # Build linked list from number of input
    ll = LinkedList() 

            
    for i in range(nop):
        while True:
            line = input(f"Enter Name & Score For Item #{i+1} (eg. Name 50.20): ").strip()
            try:
                name, data = line.rsplit(" ", 1)
                data = float(data)
                ll.insert_end(data, name)
                break
            except ValueError:
                print("Invalid Input. Please Enter Correct Format! ")

    # Ask user for sort field
    while True:
        sorted_by = input("Do You Want To Sort In (Name/Value)?: ").strip().lower()
        if sorted_by in ("name", "value"):
            break
        else:
            print("Invalid Input. Please Enter 'Name' or 'Value'! ")

    # Ask user for sort order
    while True:
        ascend = input("Do You Want To Sort Order In (Asc/Desc)? : ").strip().lower()
        if ascend in ("asc", "desc"):
            break
        else:
            print("Invalid Input. Please Enter 'asc' or 'desc'! ")

    # Convert input string to boolean
    order_arrange = (ascend == "asc")
    sort_field = "data" if sorted_by == "value" else "name"
    ll.quick_sort(order_arrange, sort_field)
    sorted_list = ll.to_array()

    # Display the sorted list
    print("\nHere Is Your Current Leaderboard:")
    for data, name in sorted_list:
        print(f"{name} = {data:.2f}")

