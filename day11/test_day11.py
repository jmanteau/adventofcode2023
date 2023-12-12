import pytest  # noqa
import day11  # noqa
from pathlib import Path
import numpy as np
import itertools

data = Path(__file__).with_name("inputdev.txt").read_text().splitlines()

data_exp = Path(__file__).with_name("inputdevexpanded.txt").read_text().splitlines()


def test_expansion():
    universe = np.array([[x for x in row] for row in data])
    universe_expanded = day11.duplicate_uniform_rows_cols(universe)
    input_universe_expanded = np.array([[x for x in row] for row in data_exp])

    assert np.array_equal(universe_expanded, input_universe_expanded)


distances = {"(2, 0)-(7, 12)": 17, "(11, 0)-(11, 5)": 5, "(0, 4)-(10, 9)": 15}


@pytest.mark.parametrize("input, expected_output", distances.items())
def test_distance(input, expected_output):
    universe_expanded = np.array([[x for x in row] for row in data_exp])
    hash_coordinates = day11.find_hash_coordinates(universe_expanded)
    # find the distance between the combination of # coordinates
    distances = {
        f"{pair[0]}-{pair[1]}": day11.manhattan_distance(pair[0], pair[1])
        for pair in itertools.combinations(hash_coordinates, 2)
    }
    assert distances[input] == expected_output


def test_part1():
    assert day11.part1(data) == 374


# def test_part2():
#    assert day11.part2(data)
