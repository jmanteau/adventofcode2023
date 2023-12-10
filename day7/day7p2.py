from collections import Counter

from loguru import logger


class Card(object):
    figure = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,
        "T": 10,
    }

    def __init__(self, card):
        self.card = card

        if self.card.isdigit():
            self.power = int(self.card)
        else:
            self.power = self.figure[self.card]

    def __str__(self):
        return f"<{self.card}>"

    def __repr__(self):
        return f"<{self.card}>"

    def __gt__(self, opposing):
        return self.power > opposing.power

    def __eq__(self, opposing):
        return self.power == opposing.power


class PokerHand(object):
    """
    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
    """

    powermap = {
        "Five of a Kind": 7,
        "Four of a Kind": 6,
        "Full House": 5,
        "Three of a Kind": 4,
        "Two Pair": 3,
        "One Pair": 2,
        "High Card": 1,
    }

    def __init__(self, cardsinput):
        self.hand = self._parse(cardsinput)
        self.raw = cardsinput
        self.power = self.powermap[self.hand]

    def _parse(self, hand):
        frequency = Counter(hand)
        counts = frequency.values()

        if 5 in counts:
            return "Five of a Kind"
        elif 4 in counts:
            if "J" in hand:
                return "Five of a Kind"
            else:
                return "Four of a Kind"
        elif 3 in counts and 2 in counts:
            return "Full House"
        elif 3 in counts:
            if hand.count("J") == 2:
                return "Five of a Kind"
            elif hand.count("J") == 2:
                return "Four of a Kind"
            else:
                return "Three of a Kind"
        elif list(counts).count(2) == 2:
            if "J" in hand:
                return "Full House"
            else:
                return "Two Pair"
        elif 2 in counts:
            if hand.count("J") == 3:
                return "Five of a Kind"
            elif hand.count("J") == 2:
                return "Four of a Kind"
            elif hand.count("J") == 1:
                return "Three of a Kind"
            else:
                return "One Pair"
        else:  # TODO check full house
            if hand.count("J") == 4:
                return "Five of a Kind"
            elif hand.count("J") == 3:
                return "Four of a Kind"
            elif hand.count("J") == 2:
                return "Three of a Kind"
            elif hand.count("J") == 1:
                return "One Pair"
            else:
                return "High Card"

    def compare_highest(self, opposing):
        # for i, opposingcard in enumerate(opposing):
        #     if self.highest[i] != opposingcard:
        #         return self.highest[i] > opposingcard
        # else:
        #     return None  # draw
        for i, opposingcard in enumerate(opposing.raw):
            if Card(self.raw[i]) != Card(opposingcard):
                return Card(self.raw[i]), Card(self.raw[i]) > Card(opposingcard)

    def __str__(self):
        return f"<{self.raw} -> {self.hand}>"

    def __repr__(self):
        return f"<{self.raw} -> {self.hand}>"

    def __gt__(self, opposing):
        if self.power > opposing.power:
            return True
        elif self.power == opposing.power:
            tiebreaker, comp = self.compare_highest(opposing)
            logger.debug(f"{self}|{opposing} wins -> {comp} with {tiebreaker}")
            return comp
        else:
            return False


def part2(data):
    logger.info("Part 2 start")

    hands = {PokerHand(line.strip().split(" ")[0]): int(line.strip().split(" ")[1]) for line in data}
    # print(sorted(hands))
    total_sum = sum(hands[hand] * (index + 1) for index, hand in enumerate(sorted(hands)))
    logger.debug(f"Total is {total_sum}")

    import ipdb

    ipdb.set_trace()
    logger.debug("Part 2 end")
    return total_sum


if __name__ == "__main__":
    DEV = False

    if DEV:
        LOGLEVEL = "DEBUG"
        inputdata = "day7/inputdev.txt"
    else:
        LOGLEVEL = "INFO"
        inputdata = "day7/input.txt"

    with open(inputdata) as file:
        data = file.readlines()

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed

    print(part2(data))


# from pathlib import Path

# data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()

# print(
#     sum(
#         (rank0 + 1) * bid
#         for rank0, (*_, bid) in enumerate(
#             sorted(
#                 (
#                     max(0, 0, *map(hand.count, set(hand) - {"J"})) + hand.count("J"),
#                     -(max(1, len(set(hand) - {"J"}))),
#                     *map("J23456789TQKA".index, hand),
#                     int(str_bid),
#                 )
#                 for hand, str_bid in map(str.split, data_raw)
#             )
#         )
#     )
# )
