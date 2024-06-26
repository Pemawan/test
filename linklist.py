
    def append (self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node.next = new_node

    def display (self):
        current = self.head

        while current :
            print(current.data, end = "-> ")

            current = current.next
        print ("none")

sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)

sll.display()