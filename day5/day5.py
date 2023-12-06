from collections import defaultdict

from loguru import logger


def parsefile1(data):
    sections = "".join(data).split("\n\n")
    seeds = []
    maps = defaultdict(list)

    for section in sections:
        title = section.split("\n")[0].split(":")[0].strip()
        logger.info(f"Parsing section {title}")
        for line in section.split("\n")[1:]:
            numbers = [int(x.strip()) for x in line.split(" ") if x]
            if title == "seeds":
                seeds = numbers
                logger.info(f"Seeds {seeds}")
            else:
                title = title.replace(" map", "")
                maps[title].append(numbers)

    return seeds, maps


def parsefile2(data):
    sections = "".join(data).split("\n\n")
    seeds = []
    maps = defaultdict(list)

    for section in sections:
        title = section.split("\n")[0].split(":")[0].strip()
        logger.debug(f"Parsing section {title}")
        for line in section.split("\n")[1:]:
            numbers = [int(x.strip()) for x in line.split(" ") if x]
            if title == "seeds":
                # logger.debug("Chunks")
                chunks = [numbers[i : i + 2] for i in range(0, len(numbers), 2)]

                # logger.debug("Ranges")

                # ranges = [range(start, start + step) for start, step in chunks]
                rangestuples = [(start, start + step - 1) for start, step in chunks]
                ranges = merge_ranges(rangestuples)

                # logger.debug("Merged")

                # merged = list(itertools.chain.from_iterable(ranges))
                seeds = ranges
                logger.debug(f"Seeds {seeds}")

            else:
                title = title.replace(" map", "")
                maps[title].append(numbers)

    return seeds, maps


def find_destination_number(source_number, mappings):
    """
    Given a source number and mappings, finds the corresponding destination number.
    """
    for dest_start, src_start, length in mappings:
        if src_start <= source_number < src_start + length:
            return dest_start + (source_number - src_start)
    return source_number  # If not in any range, it maps to itself


def map_seed_to_location(seed, all_mappings):
    """
    Maps a seed number through all categories to find the corresponding location number low end.
    """

    current_number = seed
    for category in all_mappings:
        oldnumber = current_number
        current_number = find_destination_number(current_number, all_mappings[category])
        logger.debug(f"For {category}, {oldnumber} -> {current_number}")

    return current_number


def find_destination_range(source_range, mappings):
    """
    Given a source range and mappings, finds the corresponding destination range.
    """
    src_start, src_end = source_range
    destination_ranges = []
    prev_end = src_start - 1

    for dest_start, map_src_start, length in mappings:
        map_src_end = map_src_start + length - 1

        # Check for overlap with the current mapping
        if map_src_start <= src_end and src_start <= map_src_end:
            # Calculate the overlap in the ranges and map it
            overlap_start = max(src_start, map_src_start)
            overlap_end = min(src_end, map_src_end)
            dest_range_start = dest_start + (overlap_start - map_src_start)
            dest_range_end = dest_start + (overlap_end - map_src_start)

            # Map the section before the overlap to itself, if it exists
            if prev_end < overlap_start - 1:
                destination_ranges.append((prev_end + 1, overlap_start - 1))

            destination_ranges.append((dest_range_start, dest_range_end))
            prev_end = overlap_end

    # Map the section after the last overlap to itself, if it exists
    if prev_end < src_end:
        destination_ranges.append((prev_end + 1, src_end))

    return merge_ranges(destination_ranges)


def merge_ranges(ranges):
    if not ranges:
        return []

    # Sort the ranges by their start values
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged_ranges = [sorted_ranges[0]]  # Initialize with the first range

    for current in sorted_ranges[1:]:
        last_merged = merged_ranges[-1]

        # If the current range overlaps with the last merged range, merge them
        if current[0] <= last_merged[1]:
            merged_ranges[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged_ranges.append(current)

    return merged_ranges


def map_seed_to_location_range(seed, all_mappings):
    current_range = seed
    for category in all_mappings:
        logger.debug(f"Mapping {category}")
        old_range = current_range
        current_range = find_destination_range(current_range, all_mappings[category])
        logger.info(f"For {category}, {old_range} -> {current_range}")

    return current_range


def part1(data):
    logger.info("Part 1 start")
    seeds, maps = parsefile1(data)
    lowest_location = min([map_seed_to_location(seedr, maps) for seedr in seeds])
    logger.info(f"Lowest location {lowest_location}")
    logger.debug("Part 1 end")


def part2(data):
    logger.info("Part 2 start")
    seeds, maps = parsefile2(data)
    # lowest_location = float("inf")

    lowest_location = min([map_seed_to_location_range(seed, maps) for seed in seeds])

    logger.info(f"Lowest location {lowest_location}")
    logger.debug("Part 2 end")


if __name__ == "__main__":
    DEV = True

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day5/inputdev.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day5/input.txt"

    with open(inputdata) as file:
        data = file.readlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    print(part1(data))
    print(part2(data))
