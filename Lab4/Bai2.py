# Khai báo Graph
class Graph:
    # constructor
    def __init__(self, adjacency_list, H):
        self.adjacency_list = adjacency_list
        self.H = H

    #Trả về con/hàng xóm của v
    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # Hàm Heuristic (h) chính là giá trị của node (node value)
    def h(self, n):
        return self.H[n]

    # Giải thuật A*
    def a_star_algorithm(self, start_node, end_node):
        # open_list: danh sách các node đã viếng thăm nhưng hàng xóm của chưa được viếng thăm
        #close_list: danh sách các node đã viếng thăm và hàng xóm của nó đã được viếng thăm
        open_list = set([start_node])
        closed_list = set([])

        # g chính là khoảng từ 1 node đến node khác
        # mảng g lưu trữ khoảng cách từ 1 node đến các node khác có liên kết với nó
        g = {}
        g[start_node] = 0

        #parent lưu trữ cha của node
        parents = {}
        parents[start_node] = start_node

        while open_list: #open_list khác rỗng
            n = None

            # Tìm node có giá trị hàm f() nhỏ nhất
            # biết f=g+h
            for v in open_list:
                #nếu giá trị f{v}<f{n}
                if n == None or (g[v] + self.h(v) < g[n] + self.h(n)):
                    n = v  # Compare future cost and re-assign with min cost
            if n == None:
                print("Không tìm thấy đường đi")
                return None

            # Nếu node đang xét là end_node
            if n == end_node:
                #path: lưu trữ đường đi đến 1 node
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                #Thêm vào path nút start_node
                path.append(start_node)
                #Đảo mảng
                path.reverse()
                print("Đường đi: {}".format(path))
                return path

            # Ngược lại, vòng lặp cập nhật giá trị của các con/hàng xóm
            # Cập nhật giá trị h, g ,f cho các node
            for (m, cost) in self.get_neighbors(n):
                # Nếu node đang xét chưa có trong open_list và close_list
                # Thì thêm npde vào open_list, cập nhật giá trị g và parent của node
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + cost

                # Ngược lại, nếu tìm được đường đi ngắn hơn
                # Cập nhật giá trị, parent của node
                # Nhưng nếu node này ở trong chuỗi đường đi ngắn hơn của node xét
                # thì vẫn đươc trú ra và đưa vào open_list
                else:
                    if g[m] > g[n] + cost:
                        g[m] = g[n] + cost
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # Sau khi duyệt tất cả node hàng xóm/con của node n xong,
            # đưa node n vào closed_list
            open_list.remove(n)
            closed_list.add(n)
        print("Đường đi không tồn tại")
        return None
# -----------------------------------------------------------------
adjacency_list = {
    'A': [('T', 118), ('S', 140), ('Z', 75)],
    'B': [('F', 211), ('G', 66), ('P', 100)],
    'C': [('D', 120), ('R', 146)],
    'D': [('C', 120), ('M', 75)],
    'F': [('B', 211), ('S', 99)],
    'G': [('B', 66)],
    'L': [('M', 70), ('T', 111)],
    'M': [('D', 75), ('L', 70)],
    'O': [('S', 151), ('Z', 71)],
    'P': [('B', 100), ('R', 97)],
    'R': [('C', 146), ('P', 97), ('S', 80)],
    'S': [('A', 140), ('F', 99), ('O',151),('R', 60)],
    'T': [('A', 118), ('L', 111)],
    'Z': [('A', 75), ('O', 71)],
}

heuristic = {
    'A': 366,
    'B': 0,
    'C': 160,
    'D': 242,
    'F': 178,
    'G': 77,
    'L': 244,
    'M': 241,
    'O': 380,
    'P': 98,
    'R': 193,
    'S': 253,
    'T': 329,
    'Z': 374,
}

my_graph = Graph(adjacency_list, heuristic)
my_graph.a_star_algorithm('A', 'B')
