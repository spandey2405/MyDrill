import networkx
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim,ylim
import layout
color = []
node_list = []

def Refresd_graph():
    plt.clf()
    pos = layout.get_pos(graph_obj)
    networkx.draw(graph_obj,pos,nodelist=["BR"],with_labels=True,node_size=800,node_color="blue",node_shape="p")
    networkx.draw(graph_obj,pos,nodelist=node_list,with_labels=True,node_size=600,node_color=color)
    xlim(0,200)
    ylim(0,200)
    plt.show()

def onClick(event):
    count = 0
    (x,y)   = (event.xdata, event.ydata)
    print x,y
    for i in graph_obj.nodes():
        node = pos[i]
        distance = pow(x-node[0],2)+pow(y-node[1],2)
        if distance < 20 and i != "BR":
            print "you clicked %s" % (i)

            if color[count] == "red":
                color[count] = "green"
            else:
                color[count] = "red"
        count = count + 1
    print color
    node_list = []
    Refresd_graph()
fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', onClick)

graph_obj = networkx.DiGraph()
graph_obj.add_node("BR")

for nodes in range(1,10):
    graph_obj.add_node(nodes)
    graph_obj.add_edge("BR",nodes)
    node_list.append(nodes)
    color.append("red")
pos = layout.get_pos(graph_obj)
Refresd_graph()