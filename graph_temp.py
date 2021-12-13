class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class AdjGraph:
    def __init__(self, data):
        self.data = data
        self.graph = [None] * self.data

    # Add edges
    def addEdge(self, vertice, edge):

        currNode = self.graph[vertice]  # The existing node at specified index
        newNode = Node(edge)  # Creating a new node
        if currNode == None:  # If there are no elements in this node
            self.graph[vertice] = newNode
            return

        while currNode != None:  # Traversing
            if currNode.next == None:
                currNode.next = newNode  # Attaching the New Node to the tail of the existing node
                break
            currNode = currNode.next

    # Print the graph
    def printGraph(self):
        adj_list = "Adjacency List"
        for i in range(self.data):
            adj_list += "\n\nNode " + str(i) + ": "
            temp = self.graph[i]
            while temp:
                adj_list += str(temp.vertex) + " "
                temp = temp.next
        return adj_list


ag = AdjGraph(1)
ag.addEdge(0, 0)
ag.addEdge(0, 1)
ag.addEdge(0, 2)
ag.addEdge(0, 3)
print(ag.printGraph())
# Result
# Adjacency List
# Node 0: 0 1 2 3
