import pytest  # noqa
from day1 import part1, part2, numberstoint  # noqa


def test_part1():
    lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert part1(lines) == 142  # noqa: S101


# Test cases: keys are inputs, values are expected outputs
test_cases = {
    "sevenine": "79",
    "eighthree": "83",
    "two1nine": "219",
    "eightwothree": "823",
    "abcone2threexyz": "123",
    "xtwone3four": "2134",
    "4nineeightseven2": "49872",
    "zoneight234": "18234",
    "7pqrstsixteen": "76",
}


# Test function using parametrize
@pytest.mark.parametrize("input, expected_output", test_cases.items())
def test_your_function(input, expected_output):
    assert numberstoint(input) == expected_output  # noqa: S101


def test_part2():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert part2(lines) == 281  # noqa: S101
