#Bài4
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
#1. Khai báo giải thuật Depth-First Search(DFS) Start-End

def DFS_Path(graph,start,end):
    queue=[(start,[start])]
    visited=set()
    while queue:
        node,path=queue.pop()
        if node not in visited:
            if node == end:
                return path
            visited.add(node)
        for i in graph[node]:
            node.append((i,path+[i]))
                
#2. Gọi hàm DFS
print("Duyệt đồ thị DFS: ")
start=input ("Vị trí bắt đầu là: ")
end=input ("Vị trí kết thúc là: ")
print("DFS đi từ " +start+ " đến " +end+": ")
print(DFS_Path(graph, start, end))
