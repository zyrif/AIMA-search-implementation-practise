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

romania_heuristic={
    "Arad": 366,
    "Zerind": 374,
    "Oradea": 380,
    "Timisoara": 329,
    "Lugoj": 244,
    "Mehadia": 241,
    "Dobreta": 242,
    "Craiova": 160,
    "RimnicuVilcea": 193,
    "Sibiu": 253,
    "Fagaras": 176,
    "Pitesi": 100,
    "Bucharest": 0,
    "Giurgiu": 77,
    "Urziceni": 80,
    "Hirsova": 151,
    "Eforie": 161,
    "Vaslui": 199,
    "Iasi": 226,
    "Neamt": 234
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
    def getNode(self, name):
        for i in self.data:
            if(name == i.name):
                return i
    def delNode(self, name):
        for i in self.data:
            if(name == i.name):
                self.data.remove(i)
    
    def sortQueue(self):
        index = 1
        if len(self.data)>1:
            while len(self.data)>index:
                if(self.data[index-1].pathcost > self.data[index].pathcost):
                    temp = self.data[index-1]
                    self.data[index-1] = self.data[index]
                    self.data[index] = temp
                    if(index>2):
                        index = index-2
                index = index+1

    def insert(self, el):
        self.data.append(el)
        self.sortQueue()

    def insert_all(self, el):
        for i in el:
            self.data.append(i)
        self.sortQueue()

    def first(self):
        return self.data[0]

    def remove_first(self):
        return self.data.pop(0)


class Node(object):
    def __init__(self, name, pathcost=0, parent=" "):
        self.name = name
        self.parent = parent
        self.pathcost = pathcost
    def cnode(self, name, pathcost):
        return Node(name, pathcost, self.name)
    def name(self):
        return self.name
    def parent(self):
        return self.parent
    def pathcost(self):
           return self.pathcost
    def nextnodes(self):
        return romania_map[self.name]


def astar(initial):
    goal = 'Bucharest'
    frontier = Queue()
    explored = []
    path = []
    cpath = []
    frontier.insert(Node(initial))
    
    while frontier.empty()==False:
        node = frontier.remove_first()
        explored.append(node.name)
##        path.append(node.parent + " -> " + node.name + ": " + str(node.pathcost))
        path.append({'node': node.name, 'parent': node.parent, 'pathcost': str(node.pathcost+romania_heuristic[node.name])})
        
        if(node.name == goal):
            path2 = []
            tracenode = goal

            while path:
                for i in path:
                    if i['node']==tracenode:
                        path2.append({i['node']: i['pathcost']})
                        if i['parent'] == " ":
                            path = []
                            break
                        tracenode = i['parent']
            
            path2.reverse()
            cpath = path2
        
        for i in node.nextnodes():
            if i not in explored and frontier.search(i)!=True:
                frontier.insert(node.cnode(i,node.pathcost+romania_map[node.name][i]))
            elif frontier.search(i)==True:
                chkdNode = frontier.getNode(i)
                if node.pathcost+romania_map[node.name][i]+romania_heuristic[node.name] < chkdNode.pathcost+romania_heuristic[i]:
                    frontier.delNode(chkdNode.name)
                    frontier.insert(node.cnode(i,node.pathcost+romania_map[node.name][i]))
                    
    return cpath
      
