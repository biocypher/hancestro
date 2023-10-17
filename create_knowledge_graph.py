from biocypher import BioCypher

bc = BioCypher()

ont = bc._get_ontology()
print(type(ont))

ont_graph = ont._nx_graph
print(type(ont_graph))

print(ont_graph.number_of_nodes())
print(ont_graph.number_of_edges())
print(ont_graph.nodes(data=True))
