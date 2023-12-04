import itertools
import operator
import re
from functools import reduce

import networkx as nx


def get_neighbors(i, j, M, N):
    # Set up movement offsets for non-diagonal neighbors
    offsets = [-1, 0, 1]
    # Use itertools.product to generate all combinations of offsets
    directions = list(itertools.product(offsets, repeat=2))
    # Remove the (0, 0) direction as it points to the current cell
    directions.remove((0, 0))
    neighbors = []
    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < M and 0 <= new_j < N:  # Check if the new position is valid
            neighbors.append((new_i, new_j))
    return neighbors


def parse_graph(data):
    # Create an empty graph
    G = nx.Graph()
    M = len(data[0].strip())
    N = len(data)
    for y in range(N):
        for x in range(M):
            G.add_node((x, y), tag="position")

    # Parse the line (match number OR match all execpt numbers and dots)
    parse = re.compile(r"\d+|[^\d\.]")
    for y, line in enumerate(data):
        matches = parse.finditer(line.strip())
        for match in matches:
            # Span give us the position in the string (ie x coordinates)
            span = match.span()
            value = match.group()
            nodeid = f"{y}.{span}.{value}"
            G.add_node(nodeid, name=value, tag="partnumber")
            if value[0].isdigit():
                # we link a partnumber to the positions where it is found
                for x in range(span[0], span[1]):
                    print(f"Create link betwen {nodeid} and {(x,y)} ")
                    G.add_edge(nodeid, (x, y))
            else:
                # we link a gear to all position around him
                x, _ = span
                nodeid = f"({x},{y}).{value}"
                G.add_node(nodeid, tag="gear", name=value, pos=(x, y))
                neighs = get_neighbors(x, y, M, N)
                for pos in neighs:
                    print(f"Create neigh link betwen {nodeid} and {pos} ")
                    G.add_edge(nodeid, pos)
    return G


def part1(data):
    G = parse_graph(data)
    # Identify nodes tagged with "gear"
    gear_nodes = [n for n, attr in G.nodes(data=True) if attr.get("tag") == "gear"]
    print(f"All gears node {gear_nodes}")
    # Find nodes that are two hops away and tagged with "partnumber"
    partnumber_nodes_two_hops_away = set()

    for node in gear_nodes:
        # Find nodes that are one hop away
        one_hop_away = set(G.neighbors(node))
        print(f"Current node {node}")

        # Find nodes that are two hops away
        for n in one_hop_away:
            two_hops_away = set(G.neighbors(n)) - {node} - one_hop_away  # Exclude the original node and one-hop nodes
            print({x for x in two_hops_away if G.nodes[x].get("tag") == "partnumber"})
            partnumber_nodes_two_hops_away.update({x for x in two_hops_away if G.nodes[x].get("tag") == "partnumber"})

    sumpartnumber = sum([int(G.nodes[n].get("name")) for n in partnumber_nodes_two_hops_away])

    return sumpartnumber


def part2(data):
    G = parse_graph(data)
    # Identify nodes tagged with "gear"
    gear_nodes = [n for n, attr in G.nodes(data=True) if attr.get("name") == "*"]
    print(f"All gears node {gear_nodes}")

    sum_gear_ratio = 0

    for node in gear_nodes:
        # Find nodes that are one hop away
        one_hop_away = set(G.neighbors(node))
        print(f"Current node {node}")

        partnumber_nodes_two_hops_away = set()
        # Find nodes that are two hops away
        for n in one_hop_away:
            two_hops_away = set(G.neighbors(n)) - {node} - one_hop_away  # Exclude the original node and one-hop nodes
            partnumber_nodes_two_hops_away.update({x for x in two_hops_away if G.nodes[x].get("tag") == "partnumber"})
        print(f"For {node}, the partnumber two hops away are : {partnumber_nodes_two_hops_away}")

        if len(partnumber_nodes_two_hops_away) == 2:
            print(f"{node} is a STAR GEAR")
            values = [int(G.nodes[n].get("name")) for n in partnumber_nodes_two_hops_away]
            sum_gear_ratio += reduce(operator.mul, values)

    return sum_gear_ratio


with open("day3/input.txt") as file:
    data = file.readlines()

datatest = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

print(part1(data))
print(part2(data))
