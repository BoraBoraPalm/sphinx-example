import graphviz

# Create a new Graphviz graph
dot = graphviz.Digraph(comment='Basic Graphviz Example', node_attr={'shape': 'plaintext'})

# Add nodes and edges to the graph
dot.node('A', 'Node A')
dot.node('B', 'Node B')
dot.edge('A', 'B', label='Edge from A to B')

# Save the graph as a file (e.g., in DOT format)
dot.save('example_graph.dot')

# Generate a visualization of the graph (e.g., as PNG)
dot.render('example_graph', format='svg', view=True)
#dot.view()