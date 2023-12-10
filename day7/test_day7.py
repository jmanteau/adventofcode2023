import pytest  # noqa
import day7  # noqa


inputdata = "day7/inputdev.txt"
with open(inputdata) as file:
    data = file.readlines()


def test_part1():
    assert day7.part1(data)


def test_part2():
    assert day7.part2(data)
