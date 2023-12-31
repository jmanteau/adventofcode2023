import pytest  # noqa
import day5  # noqa

inputdata = "day5/inputdev.txt"
with open(inputdata) as file:
    data = file.readlines()


def test_part1():
    assert day5.part1(data) == 35


def test_part2():
    assert day5.part2(data) == 46
