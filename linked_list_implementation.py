# Implementation of Linked List in Python
class LinkedList:

    def __init__(self, initialValue) -> None:
        """
        Declare attributes head, tail and length
        """

        self.head = {
            'value': initialValue,
            'next': None,
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        """
        Adding a new node to the end of the linked list.
        """

        newNode = {
            'value': value,
            'next': None,
        }
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
        }

        newNode['next'] = self.head
        self.head = newNode
        self.length += 1
        return self

    def insertAtPos(self, value, position):
        """
        Adding at any position in the linked list.
        """

        newNode = {
            'value': value,
            'next': None,
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
        self.length += 1

    def removeFromPos(self, position):
        """
        Removing a Node at any given position in the linked list.
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

        del currNode
        self.length -= 1

# Utility Methods

    def reverse(self):
        """
        Reversing the linked list.
        """

        if not self.head['next']:
            return

        first = self.head
        self.tail = self.head
        second = self.head['next']

        while second:
            temp = second['next']
            second['next'] = first
            first = second
            second = temp

        self.head['next'] = None
        self.head = first

        self.printLinkedList()

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
            print(item, end='->')

    def traverseToIndex(self, index):
        """
        Traverse through the Linked List until a node at a given index.
        """

        currNode = self.head
        pos = 0

        while currNode != None:
            if pos == index:
                return currNode
            currNode = currNode['next']
            pos += 1


ll = LinkedList(10)
ll.append(5)
ll.append(3)
ll.append(9)
ll.append(15)
ll.insertAtPos(22, 4)
ll.removeFromPos(0)

ll.printLinkedList()
print('Length:', ll.length)
print('Reverse:', end=' ')
ll.reverse()
