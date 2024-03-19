import networkx as nx
import matplotlib.pyplot as plt
from turing_machine_tutor.examples.leap_years import leap_years
from turing_machine_tutor.turing_machine import TuringMachine


def to_graph(tm: TuringMachine) -> nx.MultiDiGraph:
    g = nx.MultiDiGraph()
    nodes = [str(q) for q in tm.states]
    g.add_nodes_from(nodes)
    for from_, to in tm.delta.items():
        q1, sigma1 = from_.state, from_.letter
        q2, sigma2, direction = to.state, to.letter, to.direction
        transition = f"{sigma1}: {sigma2}, {direction[0]}"  # sigma1, sigma2, direction
        g.add_edge(str(q1), str(q2), transition)
    return g


def visualize_graph(g: nx.MultiDiGraph):
    ...


def some_multigraph():
    G = nx.MultiDiGraph()
    from random import randint, choice
    nodes = ["A", "B", "C", "D", "E", "F"]
    G.add_nodes_from(nodes)
    for _ in range(50):
        G.add_edge(choice(nodes), choice(nodes), randint(0, 10))
    return G


if __name__ == '__main__':
    G = to_graph(leap_years.machine)
    print(nx.drawing.nx_pydot.to_pydot(G).__str__().replace("key=", "label="))