import matplotlib.pyplot as plt
import numpy as np

def graph_editor(grid=True, grid_N = 12):

    plt.ion() # interactive mode !
    fig, ax = plt.subplots(1)

    ticks = np.linspace(0,1,grid_N)

    def init_ax():
        ax.clear()
        ax.set_xlim(0,1)
        ax.set_xticks(ticks)
        ax.set_xticklabels([])
        ax.set_ylim(0,1)
        ax.set_yticks(ticks)
        ax.set_yticklabels([])
        if grid:
            ax.grid()


    # 1st STEP

    print "Place the nodes"
    init_ax()
    fig.canvas.draw
    nodes_pos = plt.ginput(-1,timeout=-1)

    if grid:
        # project the points on the nearest grid sections
        nodes_pos = [[ticks[np.argmin([abs(u-t) for t in ticks])]
                      for u in x,y] for x,y in nodes_pos]
    nodes_posx, nodes_posy = zip(*nodes_pos)

    nodes = range(len(nodes_pos))


    # 2nd STEP

    print "Place the edges"
    fig.canvas.draw()
    edges = []

    while True:
        # This loops goes as the user selects edges, and breaks when the
        # user presses enter without having selected an edge.

        # plot the current nodes and edges
        init_ax()
        for i,j in edges:
            x1,y1 = nodes_pos[i]
            x2,y2 = nodes_pos[j]
            ax.plot([x1,x2],(y1,y2),lw=2,c='k')
        ax.scatter(nodes_posx, nodes_posy, s=30)
        fig.canvas.draw()

        l = plt.ginput(2,timeout=-1)
        if len(l) == 0: # Enter has been pressed with no selection: end.
            break
        elif len(l) == 1: # only one point has been selected
            (x1,y1),(x2,y2) = nodes_pos[edges[-1][1]], l[0]
        else:  # only one point has been selected
            (x1,y1),(x2,y2) = l

        # find the nodes nearest from the positions of the clicks
        n1 = nodes[np.argmin([(x1-x)**2+(y1-y)**2 for x,y in nodes_pos])]
        n2 = nodes[np.argmin([(x2-x)**2+(y2-y)**2 for x,y in nodes_pos])]

        if (n1,n2) in edges: # a re-selection of an edge : remove
            edges.remove((n1,n2))
        else:
            edges.append((n1,n2)) # yeah ! one new edge in the graph

    plt.ioff()

    return nodes, edges,  nodes_pos




if __name__ == '__main__':

    # AN EXAMPLE OF USE

    import networkx as nx
    import matplotlib.pyplot as plt

    # draw the graph by hand
    nodes, edges, nodes_pos = graph_editor()

    # make it a Networkx graph and plot it
    G = nx.Graph() # or nx.DiGraph() for an oriented graph
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)


    fig, ax = plt.subplots(1)
    nx.draw(G, pos = dict(zip(nodes, nodes_pos)), ax=ax )
    plt.show()
