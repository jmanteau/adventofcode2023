import pytest  # noqa
import day{{ cookiecutter.day }}  # noqa


inputdata = "day{{ cookiecutter.day }}/inputdev.txt"
with open(inputdata) as file:
    data = file.readlines()

def test_part1():
    assert day{{ cookiecutter.day }}.part1(data)


def test_part2():
    assert day{{ cookiecutter.day }}.part2(data)
