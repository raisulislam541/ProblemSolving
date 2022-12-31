class Node:
    def __init__(self, data_value):
        self.data_value = data_value
        self.next_value = None

class SingleLinkedList:
    def __init__(self, head_value=None) -> None:
        self.head_value = head_value

    def append(self, new_element):
        current = self.head_value
        if current:
            while current.next_value:
                current = current.next_value
            current.next_value = new_element
        else:
            self.head_value = new_element

    def get_position(self, position):
        cur = self.head_value
        count = 1
        while cur:
            if count == position:
                return cur
            count += 1
            cur = cur.next_value

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head_value
        if position == 1:
            self.head_value = new_element
            self.head_value.next_value = current
            return
        count = 1

        if current:
            while current:
                if count == position - 1:
                    temp  = current.next_value
                    current.next_value = new_element
                    current.next_value.next_value = temp
                    return

                count +=1
                current = current.next_value

    def delete(self, value):
        """Delete node with a given value."""
        current = self.head_value
        if current.data_value == value:
            self.head_value = current.next_value
            return
        else:
            while current:
                temp = current.next_value
                if temp and (temp.data_value == value):
                    current.next_value = current.next_value.next_value
                    return
                current = current.next_value

    def print_value(self):
        values = self.head_value
        while values:
            print("values:", values.data_value)
            values = values.next_value

# list_one = Node(1)
list_one = SingleLinkedList(Node(data_value=1))
list_two = Node(data_value=2)
list_three = Node(data_value=3)

list_one.append(list_two)
list_one.append(list_three)

# list_one.print_value()
# print(list_one.get_position(3).data_value)
list_one.insert(Node(5),1)
# print(list_one.get_position(3).data_value)

# insertion. deleting, updating next day
list_one.print_value()

list_one.delete(2)
print(list_one.get_position(2).data_value)
# print("after delete")
list_one.print_value()

