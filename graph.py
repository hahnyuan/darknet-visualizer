from graphviz import Digraph


def viz_simple(pc,format):
    g=Digraph('net',format=format)
    g.node('input_data')

    for i,layer in enumerate(pc[1:]):
        ltype=layer['type']
        if ltype=='convolutional':
            label="{}{size}x{size}\\n{num}".format(ltype,size=layer.get('size'),num=layer.get('filters'))
        else:
            label=ltype
        g.node("{}".format(i),label=label,color='red')
        if i==0:
            g.edge('input_data',str(i))
        if ltype=='shortcut':
            g.edge(str(int(layer['from'])+i),str(i))
            g.edge(str(i-1),str(i))
        elif ltype=='route':
            bottoms=layer['layers'].split(',')
            for bottom in bottoms:
                bottom=bottom.strip()
                g.edge(str(i+int(bottom)) if '-' in bottom else bottom,str(i))
        else:
            g.edge(str(i-1),str(i))
    return g