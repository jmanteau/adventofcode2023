import math
import re
import sys

import ipdb
import networkx as nx
from loguru import logger


def parse1(data):
    pattern = re.compile(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)")

    # Create a MultiDiGraph :Directed graphs with self loops and parallel edges
    G = nx.MultiDiGraph()

    # Parse the data and add edges to the graph
    for line in data:
        match = pattern.match(line)
        if match:
            node, left_node, right_node = match.groups()
            G.add_edge(node, left_node, name="L")
            G.add_edge(node, right_node, name="R")

    return G


def part1(data):
    logger.info("Part 1 start")
    directions = data[0].strip()

    graph = parse1(data[2:])
    """
    > pprint(nx.to_dict_of_dicts(graph))
    {'AAA': {'BBB': {0: {'name': 'left'}}, 'CCC': {0: {'name': 'right'}}},
    'BBB': {'DDD': {0: {'name': 'left'}}, 'EEE': {0: {'name': 'right'}}},
    'CCC': {'GGG': {0: {'name': 'right'}}, 'ZZZ': {0: {'name': 'left'}}},
    'DDD': {'DDD': {0: {'name': 'left'}, 1: {'name': 'right'}}},
    'EEE': {'EEE': {0: {'name': 'left'}, 1: {'name': 'right'}}},
    'GGG': {'GGG': {0: {'name': 'left'}, 1: {'name': 'right'}}},
    'ZZZ': {'ZZZ': {0: {'name': 'left'}, 1: {'name': 'right'}}}}
    """

    start_node = "AAA"
    target_node = "ZZZ"
    current_node = start_node
    i = 1
    while current_node != target_node:
        # Wrapped the index to repeat the directions
        wrapped_index = i % len(directions) - 1
        direction = directions[wrapped_index]
        # Find the outgoing edge with the specified attribute
        next_edge = [(u, v) for u, v, attr in graph.out_edges(current_node, data=True) if attr.get("name") == direction]
        if len(next_edge) > 1:
            logger.warning(f"MORE THAN 1 NEXT EDGE -> {len(next_edge)} for {direction}")
            ipdb.set_trace()
            sys.exit(0)
        cur, next = next_edge[0]
        logger.debug(f"{i} Following {direction} edge from {cur} to {next}")
        current_node = next
        i += 1

    steps = i - 1
    logger.info(f"Reached {target_node} in {steps} steps")

    logger.debug("Part 1 end")
    return steps


def next_node(graph, current_node, direction):
    next_edge = [(u, v) for u, v, attr in graph.out_edges(current_node, data=True) if attr.get("name") == direction]
    if len(next_edge) > 1:
        logger.warning(f"MORE THAN 1 NEXT EDGE -> {len(next_edge)} for {direction}")

        ipdb.set_trace()
    cur, next = next_edge[0]
    return next


def number_steps(graph, start_node, directions):
    i = 1
    current_node = start_node
    while not current_node.endswith("Z"):
        # Wrapped the index to repeat the directions
        wrapped_index = i % len(directions) - 1
        direction = directions[wrapped_index]
        next = next_node(graph, current_node, direction)
        current_node = next
        i += 1

    steps = i - 1
    print(f"Reached {current_node} in {steps} steps")
    return steps


def part2(data):
    logger.info("Part 2 start")
    directions = data[0].strip()

    graph = parse1(data[2:])

    start_nodes = [node for node in graph.nodes() if node.endswith("A")]
    logger.info(f"Starting from {len(start_nodes)}: {start_nodes}")
    steps = []
    for node in start_nodes:
        steps.append(number_steps(graph, node, directions))
    # we find each invidual path and get the lcm of them for when the paths are going to "align"
    logger.debug("Part 2 end")
    return math.lcm(*steps)


if __name__ == "__main__":
    DEV = False

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day8/inputdev2.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day8/input.txt"

    with open(inputdata) as file:
        data = file.readlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    #   print(part1(data))

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day8/inputdev3.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day8/input.txt"

    with open(inputdata) as file:
        data = file.readlines()

    print(part2(data))
