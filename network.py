# -*- coding: utf-8 -*-

from glob import glob
import json
import networkx as nx

namespaces = {'it': 'Utente:', 'en': 'User:', 'de': 'Benutzer:'}

project = 'it'
unamespace = namespaces[project]
thanksdir = 'thanks_%s' % project

thks = []
for filename in glob('%s/*' % thanksdir):
    with open(filename) as fp:
        thks += [json.load(fp)]

print(len(thks))

thankers = set(tnk['user'] for tnk in thks)
thanked = set(thk['title'].lstrip(unamespace) for thk in thks)
users = thanked.union(thankers)

edges = [(thk['user'], thk['title'].lstrip(unamespace),
          {'ts': thk['timestamp']})
          for thk in thks]

print(len(users), len(edges))

G = nx.DiGraph()
G.add_nodes_from(users)
G.add_edges_from(edges)
nx.write_gexf(G, '%s_digraph.gexf' % (thanksdir))
print (G.number_of_nodes(), G.number_of_edges())

U = G.to_undirected()
nx.write_gexf(U, '%s_graph.gexf' % (thanksdir))
print (U.number_of_nodes(), U.number_of_edges())

giant = max(nx.connected_component_subgraphs(U), key=len)
nx.write_gexf(giant, '%s_giant.gexf' % (thanksdir))
print (giant.number_of_nodes(), giant.number_of_edges())

