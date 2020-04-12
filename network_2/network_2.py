import pyyed

g = pyyed.Graph()


# LOC1
loc1 = g.add_group('LOC1')
loc1.add_node('R1', shape='ellipse')
loc1.add_node('R2', shape='ellipse')
loc1.add_node('MONITOR_INT', shape='octagon', shape_fill="#3311EE")

services_loc1 = g.add_group('SERVICES_LOC1')
services_loc1.add_node('s1', label='SQL', shape_fill="#8800EE")
services_loc1.add_node('m1', label='MAIL', shape_fill="#8800EE")
services_loc1.add_node('w1', label='WWW', shape_fill="#8800EE")
loc1.add_group('SERVICES_LOC1')

# LOC2
loc2 = g.add_group('LOC2')
loc2.add_node('R3', shape = 'ellipse')

services_loc2  = g.add_group('SERVICES_LOC2')
services_loc2.add_node('w2', label='WWW', shape_fill="#8800EE")
services_loc2.add_node('w3', label='WWW', shape_fill="#8800EE")
services_loc2.add_node('w4', label='WWW', shape_fill="#8800EE")
loc2.add_group('SERVICES_LOC2')

# STAND ALONE NODE 
g.add_node('MONITOR_EXT', shape='octagon', shape_fill="#3311EE")


# EDGES
g.add_edge('R1','R2', arrowhead="none")
g.add_edge('R2','R3', arrowhead="none")
g.add_edge('R3','SERVICES_LOC2', arrowhead="none", line_type="dashed")
g.add_edge('R1','SERVICES_LOC1', arrowhead="none", line_type="dashed")

g.add_edge('MONITOR_EXT','SERVICES_LOC1', arrowhead="none", line_type="dotted")
g.add_edge('MONITOR_EXT','SERVICES_LOC2', arrowhead="none", line_type="dotted")

g.add_edge('MONITOR_INT','SERVICES_LOC1', arrowhead="none", line_type="dotted")

g.write_graph('network2.graphml', pretty_print=True)
