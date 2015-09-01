__author__ = 'spandey2405'

import xlrd
import test_helper
workbook = xlrd.open_workbook('Test_Detail/Test_Detail_20-08-2015_10:40:06.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')

def get_ipv(m_name):
    a = True
    row = 1
    column = 0
    mote_name = m_name
    Mote_IPv6 = "NULL"
    while(a==True):
        Mote_Name = worksheet.cell(row, column).value
        if mote_name == Mote_Name:
            Mote_IPv6= worksheet.cell(row, column+1).value
            a=False
        row = row +1
        if (Mote_Name == "END"):
            a=False

    return Mote_IPv6

def get_mote(m_ipv6):
    a = True
    row = 1
    column = 0
    mote_ipv6 = m_ipv6
    Mote_Name = "NULL"
    while(a==True):
        Mote_IPv6 = worksheet.cell(row, column+1).value
        if mote_ipv6 == Mote_IPv6:
            Mote_Name= worksheet.cell(row, column).value
            a=False
        row = row +1
        if (Mote_Name == "END"):
            a=False

    return Mote_Name

def get_motes_from_routes(BR,endpoint):
    import get_mote_name
    get_mote_name.get_motes_detail(BR,endpoint)

def get_nodes(BR,endpoint):
    motes = []
    b = test_helper.get_data(BR,endpoint)
    for values_b in b:
        value_b = values_b.split('->')
        value_b[1] = value_b[1].split('::')[-1]
        value_b[1] = "aaaa::"+value_b[1]
        value_b[0] = get_mote(value_b[0])
        value_b[1] = get_mote(value_b[1])
        motes.append(value_b[0])
        motes.append(value_b[1])

    unique_motes = list(set(motes))

    return unique_motes

def get_edges(BR,endpoint):
    edges = []
    b = test_helper.get_data(BR,endpoint)
    for values_b in b:
        value_b = values_b.split('->')
        value_b[1] = value_b[1].split('::')[-1]
        value_b[1] = "aaaa::"+value_b[1]
        value_b[0] = get_mote(value_b[0])
        value_b[1] = get_mote(value_b[1])
        if value_b[0]==value_b[1]:
            values = "BR->"+value_b[0]
        else:
            values = value_b[0]+"->"+value_b[1]
        edges.append(values)
    return edges

def draw_graph(BR,endpoint):
    import networkx
    import matplotlib.pyplot as plt

    graph_obj = networkx.DiGraph()
    nodes = get_nodes(BR,endpoint)
    graph_obj.add_node("BR")
    for node in nodes:
        graph_obj.add_node(node)

    edges = get_nodes(BR,endpoint)

    for edge in edges:
        edge = edge.split('->')
        source = edge[0]
        destination = edge[1]
        graph_obj.add_edge(source,destination)
    pos = networkx.spring_layout(graph_obj)
    networkx.draw_networkx_labels(graph_obj, pos,font_color="black", font_size=8,font_weight='bold')
    networkx.draw(graph_obj, pos,nodelist = ["BR"], node_color="Blue", node_size=2000,node_shape="p")
    networkx.draw(graph_obj, pos,nodelist = nodes, node_color="green", node_size=600,)
    plt.show()




