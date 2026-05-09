class Graph:
    def __init__(self):
        self.adj_list = {}
        
    # def print_list(self):
    #     for vertex in self.adj_list:
    #         print(f"{vertex} : {self.adj_list[vertex]}")
            
    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
 
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False        
            
    
a = Graph()
a.add_vertex('A')
a.add_vertex('B')
a.add_vertex('C')
a.add_vertex('D')

a.add_edge('A','B')
a.add_edge('A','C')
a.add_edge('A','D')
a.add_edge('B','D')
a.add_edge('C','D')

a.remove_vertex('D')
a.print_graph()