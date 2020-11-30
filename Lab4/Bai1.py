#Bai1: Hiện thực giải thuật A* để tìm đường đi từ start_node đến end_node
#Khai báo class Graph
class Graph:
    #Contructor
    def __init__(self, adjacency_list, H):
        self.adjacency_list = adjacency_list
        self.H=H
    #Trả về con/hàng xóm của v
    def get_neighbors(self, v):
        return adjacency_list[v]
    #Hàm Heuristic (h) chính là giá trị của node (node value)
    def h(self, n):
        return H[n]

    #Giải thuật A*
    def a_start_algoithm(self, start_node, end_node):
        #open_list: danh sách các node đã viếng thăm nhưng hàng xóm của chưa được viếng thăm
        #close_list: danh sách các node đã viếng thăm và hàng xóm của nó đã được viếng thăm

        open_list=set([start_node])
        close_list=set([])

        #g chính là khoảng từ 1 node đến node khác
        #mảng g lưu trữ khoảng cách từ 1 node đến các node khác có liên kết với nó
        g = {}
        g[start_node]=0

        #parent lưu trữ cha của node
        parents = {}
        parents[start_node]=start_node

        while open_list: #open_list khác rỗng
            n = None

            #Tìm node có giá trị hàm f() nhỏ nhất
            #biết f=g+h
            for v in open_list:
                #nếu giá trị f{v}<f{n}
                if n == None or (g[v]+self.h(v) < g[n]+self.h(n)):
                    n = v #gán n=v

            if n == None:
                print("Không tìm thấy đường đi")
                return None

            #Nếu node đang xét là end_node
            if n == end_node:
                #path: lưu trữ đường đi đến 1 node
                path = []

                while parents[n] != n:
                    path.append(n)
                    n=parents[n]

                #Thêm vào path nút start_node
                path.append(start_node)
                #Đảo mảng
                path.reverse()

                print("Đường đi: {}".format(path))
                return path

            #Ngược lại, vòng lặp cập nhật giá trị của các con/hàng xóm
            #Cập nhật giá trị h, g ,f cho các node
            for(m, cost) in self.get_neighbors(n):
                #Nếu node đang xét chưa có trong open_list và close_list
                #Thì thêm npde vào open_list, cập nhật giá trị g và parent của node
                if m not in open_list and m not in close_list:
                    open_list.add(m)
                    parents[m]=n
                    g[m]=g[n]+cost

                #Ngược lại, nếu tìm được đường đi ngắn hơn
                #Cập nhật giá trị, parent của node
                #Nhưng nếu node này ở trong chuỗi đường đi ngắn hơn của node xét
                #thì vẫn đươc trú ra và đưa vào open_list
                else:
                    if  g[m]>g[n]+cost:
                        g[m]=g[n]+cost
                        parents[m]=n

                        if m in close_list:
                            close_list.remove(m)
                            open_list.add(m)
            #Sau khi duyệt tất cả node hàng xóm/con của node n xong,
            #đưa node n vào closed_list
            open_list.remove(n)
            close_list.add(n)
        print("Đường đi không tồn tại")
        return None
#--------------------------------------------------------------------
#Khai báo đồ thị
adjacency_list={
        'A':[('C', 9), ('D', 7), ('E',13),('F',20)],
        'C':[('H', 6)],
        'D':[('E', 4),('H',8)],
        'E':[('K', 4),('I',3)],
        'F':[('I', 6),('G',4)],
        'H':[('K', 5)],
        'K':[('B', 6)],
        'I':[('K', 9),('B', 5)]}
#Khai báo giá trị hàm Heuristic h()
H={
    'A':14,
    'B':0,
    'C':15,
    'D':6,
    'E':8,
    'F':7,
    'G':12,
    'H':10,
    'K':2,
    'I':4,
    }
graph1 = Graph(adjacency_list, H)
graph1.a_start_algoithm('A','B')

