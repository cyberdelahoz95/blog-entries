import math
from functools import reduce

class Node:
    def __init__(self, coordinates, children, distance):
        self.coordinates = coordinates
        self.children = children
        self.distance = distance

    def addChildren (self, children):
        self.children = children

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcEuclidianDistanceTo(self, anotherCoordinate):
        a = (anotherCoordinate.x - self.x) ** 2
        b = (anotherCoordinate.y - self.y) ** 2
        return math.sqrt(a + b)

def avg(l): 
    avg = reduce(lambda x, y: x + y, l) / len(l)
    return avg
    
def clustering(dataSet):
    if (len(dataSet) == 1) :
        return dataSet
    else :
        lowest = None
        i = 0
        index1 = None
        index2 = None
        for element1 in dataSet:
            j = 0
            for element2 in dataSet:
                currentDistance = element1.coordinates.calcEuclidianDistanceTo(element2.coordinates)
                if ((lowest != None and lowest > currentDistance) or lowest == None):
                    index1 = i
                    index2 = j
                    lowest = currentDistance
                j = j + 1
            i = i + 1
        newX = avg([ dataSet[index1].coordinates.x, dataSet[index2].coordinates.x ])
        newY = avg([ dataSet[index1].coordinates.y, dataSet[index2].coordinates.y ])
        newCoordinates = Coordinate(newX, newY)
        newNode = Node(newCoordinates, [ dataSet[index1], dataSet[index2] ], lowest)
        del dataSet[index1]
        del dataSet[index2]
        dataSet.append(newNode)
        return clustering(dataSet)

def main():
    coord1 = Coordinate(1.0, 1.0)
    coord2 = Coordinate(2.0, 2.0)
    coord3 = Coordinate(5.0, 5.0)
    coord4 = Coordinate(8.0, 8.0)
    coord5 = Coordinate(10.0, 10.0)
    node1 = Node(coord1, None, None)
    node2 = Node(coord2, None, None)
    node3 = Node(coord3, None, None)
    node4 = Node(coord4, None, None)
    node5 = Node(coord5, None, None)
    dataSet = [node1, node2, node3, node4, node5]
    cluster = clustering(dataSet)

if __name__ == "__main__":
    main()