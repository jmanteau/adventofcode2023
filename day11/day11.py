import itertools
from pathlib import Path

import numpy as np
from loguru import logger

data_exp = Path(__file__).with_name("inputdevexpanded.txt").read_text().splitlines()


def duplicate_uniform_rows_cols(arr, symbol=".", expansion_factor=1):
    expanded_arr = np.copy(arr)

    # Determine which rows and columns to duplicate
    rows_to_duplicate = [i for i in range(arr.shape[0]) if np.all(arr[i, :] == symbol)]

    # Expand the rows expansion_factor times
    for i in sorted(rows_to_duplicate, reverse=True):
        expanded_arr = np.insert(expanded_arr, i, np.repeat([expanded_arr[i, :]], expansion_factor, axis=0), axis=0)
    logger.debug("Expand row done. Now columns")

    # Expand the columns expansion_factor times
    cols_to_duplicate = [j for j in range(arr.shape[1]) if np.all(arr[:, j] == symbol)]
    for j in sorted(cols_to_duplicate, reverse=True):
        col_expanded = np.repeat(expanded_arr[:, j][:, np.newaxis], expansion_factor, axis=1)
        # Split the expanded_arr into two parts
        left_part = expanded_arr[:, :j]  # Everything before column j
        right_part = expanded_arr[:, j:]  # Everything from column j onwards

        # Horizontally stack left_part, col_expanded, and right_part
        expanded_arr = np.hstack((left_part, col_expanded, right_part))

    # for j in sorted(cols_to_duplicate, reverse=True):
    #     for _ in range(expansion_factor):
    #         expanded_arr = np.insert(expanded_arr, j, expanded_arr[:, j], axis=1)

    return expanded_arr


def find_hash_coordinates(arr):
    """Find the coordinates of all '#' characters in the array."""
    return [(i, j) for i in range(arr.shape[0]) for j in range(arr.shape[1]) if arr[i, j] == "#"]


def chebyshev_distance(point1, point2):
    """Calculate the Chebyshev distance between two points."""
    return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))


def manhattan_distance(point1, point2):
    """Calculate the Manhattan distance between two points."""
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def part1(data):
    logger.info("Part 1 start")
    universe = np.array([[x for x in row] for row in data])
    universe_expanded = duplicate_uniform_rows_cols(universe)

    hash_coordinates = find_hash_coordinates(universe_expanded)
    # find the distance between the combination of # coordinates

    distances = {
        f"{pair[0]}-{pair[1]}": manhattan_distance(pair[0], pair[1]) for pair in itertools.combinations(hash_coordinates, 2)
    }

    logger.debug("Part 1 end")
    return sum(distances.values())


def part2(data):
    logger.info("Part 2 start")
    universe = np.array([[x for x in row] for row in data])
    universe_expanded = duplicate_uniform_rows_cols(universe, expansion_factor=1000000)

    hash_coordinates = find_hash_coordinates(universe_expanded)
    # find the distance between the combination of # coordinates

    distances = {
        f"{pair[0]}-{pair[1]}": manhattan_distance(pair[0], pair[1]) for pair in itertools.combinations(hash_coordinates, 2)
    }

    logger.debug("Part 2 end")
    return sum(distances.values())


if __name__ == "__main__":
    DEV = False

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "inputdev.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "input.txt"

    data = Path(__file__).with_name(inputdata).read_text().splitlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    #  print(part1(data))
    print(part2(data))
