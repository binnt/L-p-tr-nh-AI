#Bài1
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
#1. Khai báo giải thuật Breadth-First Search(BFS) để duyệt đồ thị
def BFS(graph, start):
    queue=[start] #queuue được khai báo dạng list, giá trị ban đầu là start
    visited=[]

    while queue: #queue khác rỗng
        node=queue.pop(0) #lấy note đầu tiên trong queue
        if node in visited:
            continue
        visited.append(node)
        for next_node in graph[node]: #triển khai các con (next_node) của node
            queue.append(next_node)
    return visited
#2. Gọi hàm BFS
print("Ket qua duyet do thi(giai thuat BFS):")
print(BFS(graph,'A'))
    
