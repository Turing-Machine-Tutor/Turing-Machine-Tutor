import networkx as nx

from turing_machine_tutor.examples.leap_years import leap_years
from turing_machine_tutor.turing_machine import TuringMachine


def to_graph(tm: TuringMachine) -> nx.MultiDiGraph:
    g = nx.MultiDiGraph()
    nodes = [str(q) for q in tm.states]
    g.add_nodes_from(nodes)
    for from_, to in tm.delta.items():
        q1, sigma1 = from_.state, from_.letter
        q2, sigma2, direction = to.state, to.letter, to.direction
        transition = sigma1, sigma2, direction
        g.add_edge(str(q1), str(q2), transition)
    return g


def visualize_graph(g: nx.MultiDiGraph):
    ...


if __name__ == '__main__':
    g = to_graph(leap_years.machine)
    print(g.edges)
    pass