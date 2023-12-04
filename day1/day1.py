import regex as re


def part1(lines):
    """
    Calculate the sum of the first and last digits found in each line of the provided list of strings.

    Args:
    lines (list of str): A list of strings, each potentially containing digits.

    Returns:
    int: The sum of the first and last digits found in each line.
    """
    restr = re.compile(r"\d")
    results = []
    for line in lines:
        out = restr.findall(line)
        if out:
            results.append(int(out[0] + out[-1]))  # First digit + Last digit
    return sum(results)


def part1_codegolf(lines):
    """
    A concise version of the part1 function to calculate the same sum using a more compact syntax.

    Args:
    lines (list of str): A list of strings, each potentially containing digits.

    Returns:
    int: The sum of the first and last digits found in each line.
    """
    return sum([int(re.findall(r"\d", line)[0] + re.findall(r"\d", line)[-1]) for line in lines])


def numberstoint(line):
    """
    Convert words representing numbers in a string to their corresponding digits, keeping digit and removing other characters .

    Args:
    line (str): The string containing number words and potentially other characters.

    Returns:
    str: A string with number words replaced by their corresponding digits.
    """
    word2nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    restr = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")
    results = [word2nums[x] if not x.isdigit() else x for x in restr.findall(line, overlapped=True)]
    return "".join(results)


def numberstoint_old(line):
    """
    Recursively convert number words in a string to their digits, processing left to right uniquely.
    This function handles overlapping words, e.g., "sevenine" becomes "7ine".

    Args:
    line (str): The string to convert.

    Returns:
    str: The converted string with number words replaced by digits.
    """
    print("Starting recursion for: " + line)

    # Map words to their corresponding digits
    word2nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    nextstart = 0  # Starting index for the search window

    for i in range(len(line)):
        if i != nextstart:
            print(f"Current i:{i}. Next start at {nextstart}")
            continue

        print("Moving Window Start")
        found = False  # Flag to indicate if a match was found

        # Check different window lengths
        for windowlen in range(1, 6):
            if found:
                break

            print("Next window len")
            window = line[i : i + windowlen]
            print("W:" + window)

            for word, digit in word2nums.items():
                oldwindow = window
                window = window.replace(word, digit)

                if oldwindow != window:
                    print("Found: " + oldwindow + "->" + window)
                    # Recreate the line with the replacement
                    newline = line[:i] + window + line[i + windowlen :]
                    print("New line:" + newline)
                    # Recursive call with the updated line
                    return numberstoint_old(newline)

            # Move the start index if a match was found
            nextstart = i + len(oldwindow) - 1
            print(f"Cursor moved to {nextstart}")

        # Increment the start index if no match was found
        nextstart += 1

    return line


def part2(lines):
    """
    Process a list of strings by converting number words to digits and then calculating the sum of the first and
    last digits in the transformed strings.

    Args:
    lines (list of str): A list of strings, each potentially containing number words and digits.

    Returns:
    int: The sum of the first and last digits of the transformed strings.
    """
    results = []
    for line in lines:
        linenumbers = numberstoint(line)
        results.append(int(linenumbers[0] + linenumbers[-1]))
    return sum(results)


# Example usage
with open("input.txt") as file:
    data = file.readlines()

print("Part1:" + str(part1(data)))
print("Part1:" + str(part1_codegolf(data)))
print("Part2:" + str(part2(data)))
