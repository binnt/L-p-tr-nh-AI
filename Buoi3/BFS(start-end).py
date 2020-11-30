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
#1. Khai báo giải thuật Breadth-First Search(BFS) để in từ start đến end
def BFS_Path(graph, start, end):
    queue=[(start, [start])] #queue được khai báo dạng list, giá trị ban đầu là start và cha của start

    while queue: #queue khác rỗng
        node, path=queue.pop(0) #lấy note đầu tiên trong queue
        for next_node in graph[node]: #triển khai các con (next_node) của node
            if next_node in path:
                continue
            elif next_node == end:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node])) #queue lưu giá trị của next_node và đường dẫn đến next_node
                
#2. Gọi hàm BFS_Path
start = input('Nhập vị trí start = ')
end = input('Nhập vị trí end = ')
print("Đường đi từ "+start+" đến "+end+" : ")
print(BFS_Path(graph, start, end))
                
    
    


    
