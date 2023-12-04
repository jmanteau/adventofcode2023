import pytest  # noqa
from day2 import part1, part2, parse_game, game_valid, Color, game_power  # noqa
from collections import Counter


input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_parse_game():
    line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    game_nb = "3"
    results = [
        [
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.BLUE,
            Color.BLUE,
            Color.BLUE,
            Color.BLUE,
            Color.BLUE,
            Color.BLUE,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
        ],
        [
            Color.BLUE,
            Color.BLUE,
            Color.BLUE,
            Color.BLUE,
            Color.BLUE,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.RED,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
            Color.GREEN,
        ],
        [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED],
    ]
    assert parse_game(line) == (game_nb, results)  # noqa: S101


test_cases_valid = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


@pytest.mark.parametrize("line", test_cases_valid)
def test_game_valid_true(line):
    MAX_COUNT = Counter({Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14})
    game, results = parse_game(line)
    assert game_valid(results, MAX_COUNT)  # noqa: S101


test_cases_invalid = [
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
]


@pytest.mark.parametrize("line", test_cases_invalid)
def test_game_valid_false(line):
    MAX_COUNT = Counter({Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14})
    game, results = parse_game(line)
    assert not game_valid(game, MAX_COUNT)  # noqa: S101


def test_part1():
    data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    ]
    assert part1(data) == 8


power_test_cases = {
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green": 48,
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue": 12,
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green": 36,
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red": 1560,
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red": 630,
}


@pytest.mark.parametrize("line, power", power_test_cases.items())
def test_game_power(line, power):
    game, results = parse_game(line)
    assert game_power(results) == power


def test_part2():
    data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    ]
    assert part2(data) == 2286
