import matplotlib.pyplot as plt
import networkx
from loguru import logger

NEXT_PIPE = {
    "|": {(0, 1), (0, -1)},
    "-": {(1, 0), (-1, 0)},
    "L": {(0, -1), (1, 0)},
    "J": {(0, -1), (-1, 0)},
    "7": {(-1, 0), (0, 1)},
    "F": {(0, 1), (1, 0)},
}


def generate_graph(layout):
    G = networkx.Graph()  # Use an undirected graph to represent the loop
    start = None
    node_map = {}  # Mapping from (x, y) to nodeid
    for y, row in enumerate(layout):
        for x, cell in enumerate(row):
            nodeid = y * len(row) + x
            node_map[(x, y)] = nodeid
            if cell == "S":
                start = nodeid
            elif cell in NEXT_PIPE:
                for dx, dy in NEXT_PIPE[cell]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in node_map:
                        G.add_edge(nodeid, node_map[(nx, ny)])
    return G, start


def find_farthest_point(G, start):
    # Find the farthest point from the start position
    lengths = networkx.single_source_shortest_path_length(G, start)
    farthest_point = max(lengths, key=lengths.get)
    return lengths[farthest_point]


def part1(data):
    logger.info("Part 1 start")
    G, start = generate_graph(data)
    max_distance = find_farthest_point(G, start)
    plt.figure(figsize=(8, 8))
    networkx.draw(G, with_labels=True, node_size=700, node_color="skyblue", font_size=15)
    plt.title("Pipe Network")
    plt.show()
    logger.debug("Part 1 end")
    return max_distance


def part2(data):
    logger.info("Part 2 start")
    logger.debug("Part 2 end")


if __name__ == "__main__":
    DEV = True

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day10/inputdev2.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day10/input.txt"

    with open(inputdata) as file:
        data = [line.strip() for line in file.readlines()]

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)

    print(part1(data))
    print(part2(data))
