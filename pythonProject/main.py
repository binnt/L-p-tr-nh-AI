# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Khai baows class Graph
class Graph:
    # constructor
    def _init_(self, adjacency_list, H):
        self.adjacency_list = adjacency_list
        self.H = H

    # Trả về con/hàng xóm của v
    def get_neighbors(self, v):
        return adjacency_list[v]

    # Hàm Heuristic (h) chính là giá trị của node (node value)
    def h(self, n):
        return H[n]

    # Giải thuật A*
    def a_start_algroithm(self, start_node, end_node):
        # Open_list: Danh sách các node đã viếng thăm nhưng hàng xóm của nó chưa được viếng thăm
        # Close_list: Danh sách các node đã viếng thăm và hàng xóm của nó đã được viếng thăm

        open_list = set([start_node])
        closed_list = set([])

        # g chính là khoảng từ 1 node đến node khác
        # mảng g lưu trữ khoảng cách từ 1 node đến các node khác có liên kết với nó
        g = {}
        g = [start_node] = 0

        # parent lưu trữ cha của node
        parent = {}
        parent[start_node = start_node

        while open_list:  # open_list khác rỗng
            n = Node

            # Tìm node có giá trị hàm f() nhỏ nhất
            # Biết f=g+h
            for v in open_list:
                # Nếu giá trị f{v}<f{n}
                if n == None or (g[v] + self.h(v) < g[n] + self.h(n)):
                    n = v  # gán n=v
    # Tìm node có giá trị hàm f() nhỏ nhất

