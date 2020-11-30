#Bai3
#Khai báo đồ thị
graph = {'A':['B', 'C'],
         'B':['D', 'E'],
         'C':['E', 'I'],
         'D':['F'],
         'E':['F', 'J'],
         'F':['G', 'H'],
         'G':[],'H':[],
         'I':['K'],
         'J':[],'K':[]
         }
#1. Khai báo giải thuật Depth-First Search(DFS) để duyệt đồ thị

def DFS(graph, start, visited):
    if start not in visited:
        visited.append(start)
    for neighbour in graph[start]:
        DFS(graph, neighbour , visited)
    return visited
visited=DFS(graph,'A',[])
                
#2. Gọi hàm DFS
print("Ket qua duyet do thi(giai thuat DFS):")
print(visited)
    
