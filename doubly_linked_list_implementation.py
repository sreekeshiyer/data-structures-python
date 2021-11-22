# Implementation of Doubly Linked List in Python

class DoublyLinkedList:

    def __init__(self, initialValue) -> None:
        """
        Declare attributes head, tail and length.
        """
        self.head = {
            'value': initialValue,
            'next': None,
            'prev': None,
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        """
        Adding a new node at the end of the linked list
        """

        newNode = {
            'value': value,
            'next': None,
            'prev': None,
        }
        newNode['prev'] = self.tail
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        """
        Adding a new node at the beginning of the linked list.
        """

        newNode = {
            'value': value,
            'next': None,
            'prev': None,
        }

        newNode['next'] = self.head
        self.head = newNode
        self.length += 1
        return self

    def insertAtPos(self, value, position):
        """
        Adding a new node at any given position of the linked list.
        """

        newNode = {
            'value': value,
            'next': None,
            'prev': None,
        }

        if position >= self.length:
            self.append(value)
            return self

        if position == 0:
            self.prepend(value)
            return self

        prevNode = self.traverseToIndex(position-1)
        currNode = prevNode['next']

        prevNode['next'] = newNode
        newNode['next'] = currNode
        newNode['prev'] = prevNode
        self.length += 1

    def removeFromPos(self, position):
        """
        Remove a node from any given position in the linked list.
        """

        prevNode = self.traverseToIndex(
            position-1) if position > 0 else self.head
        currNode = prevNode['next']

        if position >= self.length:
            print('Invalid position')
            return

        elif position == 0:
            self.head = currNode

        elif position == self.length - 1:
            prevNode['next'] = None
            self.tail = prevNode

        else:
            prevNode['next'] = currNode['next']
            currNode['next']['prev'] = prevNode

        del currNode
        self.length -= 1

# Utility Methods

    def printLinkedList(self):
        """
        Printing the Linked List
        """

        array = []

        currNode = self.head

        while currNode != None:
            array.append(currNode['value'])
            currNode = currNode['next']

        for item in array:
            if array.index(item) == len(array) - 1:
                print(item)
                break
            print(item, end=' ⇆ ')

    def traverseToIndex(self, index):
        """
        Traverse through the Doubly Linked List until finding a node at a given index.
        """

        isInFirstHalf = index < (self.length)/2

        if isInFirstHalf:
            pos = 0
            currNode = self.head
        else:
            pos = self.length - 1
            currNode = self.tail

        if isInFirstHalf:
            while currNode != None:
                if pos == index:
                    return currNode
                currNode = currNode['next']
                pos = pos + 1
        else:
            while currNode != None:
                if pos == index:
                    return currNode
                currNode = currNode['prev']
                pos = pos - 1


ll = DoublyLinkedList(10)
ll.append(5)
ll.append(3)
ll.append(9)
ll.append(15)
ll.append(35)
ll.prepend(25)
ll.append(45)
ll.insertAtPos(22, 4)
ll.removeFromPos(5)

ll.printLinkedList()
# 10 ⇆ 5 ⇆ 3 ⇆ 9 ⇆ 22 ⇆ 15
print('Length:', ll.length)
