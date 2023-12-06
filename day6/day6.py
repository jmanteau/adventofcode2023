import operator
from functools import reduce
from math import sqrt

from loguru import logger


def parsefile(data):
    times = [int(x.strip()) for x in data[0].split(":")[1].split(" ") if x.strip()]
    distances = [int(x.strip()) for x in data[1].split(":")[1].split(" ") if x.strip()]
    return dict(zip(times, distances))


def parsefile2(data):
    times = [x.strip() for x in data[0].split(":")[1].split(" ") if x.strip()]
    distances = [x.strip() for x in data[1].split(":")[1].split(" ") if x.strip()]
    return (int("".join(times)), int("".join(distances)))


def nb_way(totaltime, totaldistance):
    distances = []
    for time in range(0, totaltime + 1):
        distance = (totaltime - time) * time
        distances.append(distance)
        # logger.debug(f"for {time}, the distance is {distance}")

    return len([d for d in distances if d > totaldistance])


def part1(data):
    logger.info("Part 1 start")
    races = parsefile(data)

    nbways = []
    for distance, time in races.items():
        nbways.append(nb_way(distance, time))
    logger.debug("Part 1 end")
    return reduce(operator.mul, nbways)


def part2(data):
    logger.info("Part 2 start")
    race = parsefile2(data)
    time, distance = race
    # nb = nb_way(time, distance)
    nb = int(sqrt(time * time - 4 * distance))
    logger.debug("Part 2 end")

    return nb


if __name__ == "__main__":
    DEV = False

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day6/inputdev.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day6/input.txt"

    with open(inputdata) as file:
        data = file.readlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    print(part1(data))
    print(part2(data))
