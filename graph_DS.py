from collections import deque
vertices = {"A", "B", "C", "D", "E", "F"}
edges = {("A", "D"), ("A", "B"), ("A", "E"), ("A", "F"), ("B", "F"), ("B", "C")}
graph = dict()
for vertex in vertices:
    graph[vertex] = []
for edge in edges:
    v1,v2 = edge
    graph[v1].append(v2)
    graph[v2].append(v1)

bfslist = []
visitedmap =dict()
def Bfs(source):
    
    q = deque()
    visited = [False]*max(len(graph),1)
    vertices1 = list(vertices)
    for i in range(len(vertices1)):
        visitedmap[vertices1[i]] = False
    print(visitedmap)
    q.append(source)
    
    while q:
        s = q.popleft()
        print(s)
        bfslist.append(s)
        visitedmap[s]=True
        for nodes in graph[s]:
            if visitedmap[nodes]==False:
                q.append(nodes)
                print("Q",q)
                visitedmap[nodes]=True
    print(bfslist)

Bfs("A")        

    
    

print(graph)
