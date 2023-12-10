import pytest  # noqa
import day10  # noqa


inputdata = "day10/inputdev.txt"
with open(inputdata) as file:
    data = file.readlines()


def test_part1():
    assert day10.part1(data)


def test_part2():
    assert day10.part2(data)
