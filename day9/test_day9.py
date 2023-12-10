import pytest  # noqa
import day9  # noqa


inputdata = "day9/inputdev.txt"
with open(inputdata) as file:
    data = file.readlines()

finite_test_cases = [
    ([0, 3, 6, 9, 12, 15], 18),
    ([1, 3, 6, 10, 15, 21], 28),
    ([10, 13, 16, 21, 30, 45], 68),
    ([0, 1, 1, 0], -2),
]


@pytest.mark.parametrize("input, expected_output", finite_test_cases)
def test_finite(input, expected_output):
    assert day9.pred_finite_diffs(input) == expected_output


def test_part1():
    assert day9.part1(data) == 114


def test_part2():
    assert day9.part2(data) == 2
