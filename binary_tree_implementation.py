# Implementation of a Binary Tree in Python
import json


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getNode(self):
        return {
            "value": self.value,
            "left": None,
            "right": None
        }


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value):

        newNode = Node(value).getNode()

        if self.root == None:
            self.root = newNode
            return self

        currNode = self.root

        while True:
            if value < currNode["value"]:
                if not currNode["left"]:
                    currNode["left"] = newNode
                    return self
                currNode = currNode["left"]
            else:
                if not currNode["right"]:
                    currNode["right"] = newNode
                    return self
                currNode = currNode["right"]

    def lookup(self, value):
        if self.root == None:
            return None

        currNode = self.root

        while currNode:
            if value < currNode["value"]:
                currNode = currNode["left"]
            elif value > currNode["value"]:
                currNode = currNode["right"]
            elif value == currNode["value"]:
                return currNode


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(15)
tree.insert(170)
tree.insert(1)

print(json.dumps(tree.root))

#             9
#        4          20
#    1      6   15     170
