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
    def __init__(self, name, parent=" "):
        self.name = name
        self.parent = parent
    def cnode(self, name):
        return Node(name, self.name)
    def name(self):
        return self.name
    def parent(self):
        return self.parent
    def nextnodes(self):
        return romania_map[self.name]


def bfs(initial, goal):
    frontier = Queue()
    explored = []
    path = []
    frontier.insert(Node(initial))

    
    while frontier.empty()==False:
        node = frontier.remove_first()
        explored.append(node.name)
        path.append({'node': node.name, 'parent':node.parent})
        
        if(node.name == goal):
            print('Goal reached!')
            path2 = []
            path2.append(goal)
            tracenode = goal
            
            while path:
                for i in path:
                    if i['node']==tracenode:
                        if i['parent'] == " ":
                            path = []
                            break
                        path2.append(i['parent'])
                        tracenode = i['parent']


            path2.reverse()        
            return path2
        
        for i in node.nextnodes():
            if i not in explored and frontier.search(i)!=True:
                frontier.insert(node.cnode(i))
    return None
      
