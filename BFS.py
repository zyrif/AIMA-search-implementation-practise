romania_map ={
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

class Queue(object):
    """Simple FIFO queue"""
    def __init__(self, el=None):
        self.data = []
        if el:
            self.data.append(el)

    def empty(self):
        return True if len(self.data)==0 else False

    def search(self, x):
        for i in self.data:
            if(x == i.name):
                return True

    def insert(self, el):
        self.data.append(el)

    def insert_all(self, el):
        for i in el:
            self.data.append(i)

    def first(self):
        return self.data[0]

    def remove_first(self):
        return self.data.pop(0)

class Node(object):
    """call the constructor to create the initial node, cnode to create and return a child node object of the calling object..."""
    """...name and parents are self explanatory and nextnodes returns it's children (if any) as strings"""
    def __init__(self, name, parent=" "):
        self.name = name
        self.parent = parent
    def cnode(self, name):
        return Node(name, parent=self.name)
    def name(self):
        return self.name
    def parent(self):
        return self.parent
    def nextnodes(self):
##        return {'name': romania_map[self.name],'parent': self.name}
        return romania_map[self.name]


def bfs(initial, goal):
    """frontier is the primary data structure used by bfs: a fifo queue. Explored keeps track of the visited nodes so they don't make a comeback..."""
    """and path is used to calculate the return back path from goal to the inital node."""
    frontier = Queue()
    explored = []
    path = []
    frontier.insert(Node(initial))
    
##    frontier.insert_all(node.nextnodes())
##    for i in node.nextnodes():
##        frontier.insert(node.cnode(i,node.name))
##    explored.append(node.name)
    
    while frontier.empty()==False:
##        print(frontier.remove_first().name)
        node = frontier.remove_first()
        explored.append(node.name)
##        path.append(node.parent + " -> " + node.name)
        path.append({'node': node.name, 'parent':node.parent})
        for i in node.nextnodes():
            if i not in explored and frontier.search(i)!=True:
                if(node.name == goal):
##                    print('Goal reached!')
                    path2 = []
                    path2.append(goal)
                    tracenode = goal
                    
                    while path:
##                        print('Entered while loop:')
                        for i in path:
##                            print('in for loop for value:'+str(i))
                            if i['node']==tracenode:
##                                print('Entered condition for '+i['node'])
                                path2.append(i['parent'])
                                tracenode = i['parent']
                            elif tracenode == initial:
                                path = []
                                break

                    path2.reverse()        
                    return path2
                frontier.insert(node.cnode(i))
    return None
      
