import operator
from collections import Counter
from enum import Enum
from functools import reduce


class Color(str, Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"


def parse_game(line):
    game_nb = line.strip().split(":")[0].split(" ")[-1]
    results = []
    for data in line.strip().split(":")[1].split(";"):
        game = []
        for draw in data.split(","):
            number = draw.strip().split(" ")[0]
            color = Color(draw.strip().split(" ")[1])
            for _i in range(int(number)):
                game.append(color)
        results.append(game)

    return game_nb, results


def game_valid(game, MAX_COUNT):
    rounds_are_within_limit = []

    for round in game:
        color_counts = Counter(round)
        round_is_within_limit = all([count <= MAX_COUNT[color] for color, count in color_counts.items()])
        rounds_are_within_limit.append(round_is_within_limit)
    return all(rounds_are_within_limit)


def game_power(game):
    color_counts = [Counter(round) for round in game]
    minballs = [max([round[color] for round in color_counts]) for color in Color]

    return reduce(operator.mul, minballs)


def part1(data):
    MAX_COUNT = Counter({Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14})

    games = {}
    for line in data:
        game, results = parse_game(line)
        games[game] = results

    sumid = sum([int(nbgame) for nbgame, results in games.items() if game_valid(results, MAX_COUNT)])

    return sumid


def part2(data):
    games = {}
    result = 0
    for line in data:
        game, results = parse_game(line)
        games[game] = results
        result += game_power(results)
    return result


with open("day2/input.txt") as file:
    data = file.readlines()
print(part1(data))


print(part2(data))
