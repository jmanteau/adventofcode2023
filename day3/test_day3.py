import pytest  # noqa
import day3  # noqa


data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def test_part1():
    assert day3.part1(data) == 4361


def test_part2():
    assert day3.part2(data) == 467835
