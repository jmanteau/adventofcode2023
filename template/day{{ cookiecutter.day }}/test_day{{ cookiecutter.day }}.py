import pytest  # noqa
import day{{ cookiecutter.day }}  # noqa
from pathlib import Path


inputdata = "inputdev.txt"
data = Path(__file__).with_name(inputdata).read_text().splitlines()

def test_part1():
    assert day{{ cookiecutter.day }}.part1(data)


def test_part2():
    assert day{{ cookiecutter.day }}.part2(data)
