from pathlib import Path

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
        inputdata = "inputdev.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "input.txt"

    data = Path(__file__).with_name(inputdata).read_text().splitlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    print(part1(data))
    print(part2(data))
