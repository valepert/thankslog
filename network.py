# -*- coding: utf-8 -*-

from glob import glob
import json
import networkx as nx

project = 'it'
unamespace = 'Utente:'
thanksdir = 'thanks_%s' % project

thks = []
for filename in glob('%s/*' % thanksdir):
    with open(filename) as fp:
        thks += [json.load(fp)]

thankers = set(tnk['user'] for tnk in thks)
thanked = set(thk['title'].lstrip(unamespace) for thk in thks)
users = thanked.union(thankers)

edges = [(thk['user'], thk['title'].lstrip(unamespace),
          {'ts': thk['timestamp']})
          for thk in thks]

G = nx.DiGraph()
G.add_nodes_from(users)
G.add_edges_from(edges)

