import pytest  # noqa
import day6  # noqa


inputdata = "day6/inputdev.txt"
with open(inputdata) as file:
    data = file.readlines()

# Test cases: keys are inputs, values are expected outputs
test_cases = {
    (7, 9): 4,
    (15, 40): 8,
    (30, 200): 9,
}


# Test function using parametrize
@pytest.mark.parametrize("input, expected_output", test_cases.items())
def test_nbway(input, expected_output):
    time, distance = input
    assert day6.nb_way(time, distance) == expected_output  # noqa: S101


def test_part1():
    assert day6.part1(data) == 288


def test_part2():
    assert day6.part2(data) == 71503
