from loguru import logger


def part1(data):
    logger.info("Part 1 start")
    logger.debug("Part 1 end")


def part2(data):
    logger.info("Part 2 start")
    logger.debug("Part 2 end")


if __name__ == "__main__":
    DEV = True

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day10/inputdev.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day10/input.txt"

    with open(inputdata) as file:
        data = file.readlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    print(part1(data))
    print(part2(data))
