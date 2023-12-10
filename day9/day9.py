from loguru import logger


def pred_finite_diffs(values):
    matrix = [[]]
    matrix[0] = values
    line = values
    while not all([x == 0 for x in line]):
        lnext = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        line = lnext[:]  # shallow copy
        matrix.append(line)

    matrix[-1].append(0)  # we append to zero
    matrix.reverse()  # we reverse the matrix to iterate from bottom to up
    for i in range(len(matrix) - 1):
        matrix[i + 1].append(matrix[i][-1] + matrix[i + 1][-1])

    return matrix[-1][-1]


def pdebug():
    logger.info("Debug start")
    ret = pred_finite_diffs([0, 3, 6, 9, 12, 15])
    ret = pred_finite_diffs([0, 1, 1, 0])
    logger.info(f"Debug end: {ret}")


def part1(data):
    logger.info("Part 1 start")
    preds = [x.strip().split(" ") for x in data]
    next_values = []
    for values in preds:
        next = pred_finite_diffs([int(x) for x in values])
        next_values.append(next)

    logger.debug("Part 1 end")
    return sum(next_values)


def part2(data):
    logger.info("Part 2 start")

    preds = [x.strip().split(" ") for x in data]
    next_values = []

    for values in preds:
        input = [int(x) for x in values]
        input.reverse()
        next = pred_finite_diffs(input)
        next_values.append(next)

    logger.debug("Part 2 end")
    return sum(next_values)


if __name__ == "__main__":
    DEV = False

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day9/inputdev.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day9/input.txt"

    with open(inputdata) as file:
        data = file.readlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    # pdebug()
    print(part1(data))
    print(part2(data))
