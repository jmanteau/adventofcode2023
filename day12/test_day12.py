import pytest  # noqa
import day12  # noqa
from pathlib import Path


inputdata = "inputdev.txt"
data = Path(__file__).with_name(inputdata).read_text().splitlines()


def test_part1():
    assert day12.part1(data)


def test_part2():
    assert day12.part2(data)
