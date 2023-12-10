import pytest  # noqa
import day8  # noqa


inputdata = "day8/inputdev.txt"
with open(inputdata) as file:
    data = file.readlines()


def test_part1_1():
    inputdata = "day8/inputdev.txt"
    with open(inputdata) as file:
        data = file.readlines()
    assert day8.part1(data) == 2


def test_part1_2():
    inputdata = "day8/inputdev2.txt"
    with open(inputdata) as file:
        data = file.readlines()
    assert day8.part1(data) == 6


def test_part2():
    inputdata = "day8/inputdev3.txt"
    with open(inputdata) as file:
        data = file.readlines()
    assert day8.part2(data) == 6
