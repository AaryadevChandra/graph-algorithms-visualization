import networkx as nx
import matplotlib.pyplot as plt
import pylab



node_colors_hash={}
node_colors=[]
dag = nx.digraph.DiGraph()
graph = { 0 : [],
          1 : [],
          2 : [3],
          3 : [1],
          4 : [0,1],
          5 : [0,2]
        } 

dag.add_nodes_from([0, 1, 2, 3, 4, 5])

dag.add_edges_from([(5, 2), (5, 0), (4, 0), (4, 1),
                      (2, 3),(3, 1)])


nodes=list(dag.nodes)
edges=dict(dag.edges) 

o=len(nodes)
def draw_graph(graph, node_size):
    global node_colors, node_colors_hash
    global dag
    global nodes
    global edges
   
   
    node_colors_hash = {x:"green" for x in nodes}

    for k,v in node_colors_hash.items():
        node_colors.append(v)
   
    pos = nx.shell_layout(dag)
    nx.draw(dag, pos, with_labels=True,node_size = 800, node_color=node_colors)                        
    # show graph
    pylab.show
    plt.pause(5)


def topologicalSortfunc(g, v, visited, stack):
        global graph
        global nodes
        change_node_color('gray', nodes[v])
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in graph[v]:
            #print(i)
            if visited[i] == False:
                topologicalSortfunc(g,i, visited, stack)
        change_node_color('blue', nodes[v])
        # Push current vertex to stack which stores result
        stack.append(v)


def topologicalSort(g):
        global nodes
        global o
        # Mark all the vertices as not visited
        visited = [False]*o
        stack = []
 
        # Call the recursive function to store Topological Sort starting from all vertices one by one
        for i in range(0,o):
            if visited[i] == False:
                topologicalSortfunc(g,i, visited, stack)
 
        # Print contents of the stack
        print('The Topological Sort for the following graph is :-',stack[::-1])

def change_node_color(c, node):
    global node_colors_hash
    global node_colors
    global edge_colors,edge_colors_hash
    node_colors = []

    # Color the visited node
    node_colors_hash[node]=c

    for k,v in node_colors_hash.items():
        node_colors.append(v)
    
    pos = nx.shell_layout(dag)
    nx.draw(dag, pos,node_size = 800, node_color = node_colors)
    pylab.draw()
    plt.pause(2)
    
print(nodes)    
draw_graph(dag,len(dag.edges))
topologicalSort(dag)
plt.pause(12)  
                           