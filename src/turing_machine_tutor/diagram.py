import networkx as nx
from turing_machine_tutor.turing_machine import TuringMachine


def to_graph(tm: TuringMachine) -> nx.MultiDiGraph:
    g = nx.MultiDiGraph()
    nodes = [str(q) for q in tm.states]
    g.add_nodes_from(nodes)
    for ((q1, sigma1), (q2, sigma2, direction)) in tm.delta.items():
        transition = dict(read=sigma1, write=sigma2, direction=direction)
        g.add_edge(str(q1), str(q2), transition)
    return g


def visualize_graph(g: nx.MultiDiGraph):
    ...


if __name__ == '__main__':
    g = to_graph()