import pyyed

g = pyyed.Graph()

loc1 = g.add_group('LOC1')
loc1.add_node('R1', shape='ellipse')
loc1.add_node('R2', shape='ellipse')


loc2 = g.add_group('LOC2')
loc2.add_node('R3', shape = 'ellipse')

services = g.add_group('SERVICES')
services.add_node('DNS', shape_fill="#8800EE")
services.add_node('MAIL', shape_fill="#8800EE")
services.add_node('WWW', shape_fill="#8800EE")
loc2.add_group('SERVICES')


g.add_edge('R1','R2', arrowhead="none")
g.add_edge('R2','R3', arrowhead="none")
g.add_edge('R3','SERVICES', arrowhead="none", line_type="dashed")

g.write_graph('network.graphml', pretty_print=True)

'''
RESULTING CONSENSED graphml structure
-------------------------------------

<graphml xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
    <key for="node" id="data_node" yfiles.type="nodegraphics"/>
    <key for="edge" id="data_edge" yfiles.type="edgegraphics"/>
    <graph edgedefault="directed" id="G">
        <node id="LOC1" yfiles.foldertype="group">
            <data key="data_node"></data>
            <graph edgedefault="directed" id="LOC1">
                <node id="R1"></node>
                <node id="R2"></node>
            </graph>
        </node>
        <node id="LOC2" yfiles.foldertype="group">
            <data key="data_node"></data>
            <graph edgedefault="directed" id="LOC2">
                <node id="R3"></node>
                <node id="SERVICES" yfiles.foldertype="group"></node>
            </graph>
        </node>
        <node id="SERVICES" yfiles.foldertype="group">
            <data key="data_node"></data>
            <graph edgedefault="directed" id="SERVICES">
                <node id="DNS"></node>
                <node id="MAIL"></node>
                <node id="WWW"></node>
            </graph>
        </node>
        <edge id="1" source="R1" target="R2"></edge>
        <edge id="2" source="R2" target="R3"></edge>
        <edge id="3" source="R3" target="SERVICES"></edge>
    </graph>
</graphml>

'''
