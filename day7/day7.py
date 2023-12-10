from collections import Counter

from loguru import logger


class Card(object):
    figure = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }

    def __init__(self, card):
        self.card = card

        if self.card.isdigit():
            self.power = int(self.card)
        else:
            self.power = self.figure[self.card]

    def __str__(self):
        # Used when string conversion
        return f"<{self.card}>"

    def __repr__(self):
        # Used when terminal representation (ie when printing a list of objects)
        return f"<{self.card} : {self.power}>"

    def __gt__(self, opposing):
        # greater than
        return self.power > opposing.power

    def __eq__(self, opposing):
        # equality
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
        self.highest, self.hand = self._parse(cardsinput)
        self.raw = cardsinput
        self.power = self.powermap[self.hand]

    def _parse(self, hand):
        frequency = Counter(hand)
        counts = frequency.values()

        if 5 in counts:
            highest = Card(hand[0])
            return highest, "Five of a Kind"
        elif 4 in counts:
            remains = {k: v for k, v in frequency.items() if v != 4}
            highest = sorted([Card(x) for x in remains], reverse=True)
            return highest, "Four of a Kind"
        elif 3 in counts and 2 in counts:
            highest = max([Card(x) for x in hand])
            return highest, "Full House"
        elif 3 in counts:
            # remains = {k: v for k, v in frequency.items() if v != 3}
            # highest = sorted([Card(x) for x in remains], reverse=True)
            scored = {k: v for k, v in frequency.items() if v == 3}
            for k in scored:
                hand = hand.replace(k, "")
            highest = [Card(x) for x in hand]
            return highest, "Three of a Kind"
        elif list(counts).count(2) == 2:
            # remains = {k: v for k, v in frequency.items() if v != 2}
            # highest = sorted([Card(x) for x in remains], reverse=True)
            scored = {k: v for k, v in frequency.items() if v == 2}
            for k in scored:
                hand = hand.replace(k, "")
            highest = [Card(x) for x in hand]
            return highest, "Two Pair"
        elif 2 in counts:
            # remains = {k: v for k, v in frequency.items() if v != 2}
            # highest = sorted([Card(x) for x in remains], reverse=True)
            scored = {k: v for k, v in frequency.items() if v == 2}
            for k in scored:
                hand = hand.replace(k, "")
            highest = [Card(x) for x in hand]
            return highest, "One Pair"
        else:
            # highest = sorted([Card(x) for x in hand], reverse=True)
            highest = [Card(x) for x in hand]
            return highest, "High Card"

    def compare_highest(self, opposing):
        # for i, opposingcard in enumerate(opposing):
        #     if self.highest[i] != opposingcard:
        #         return self.highest[i] > opposingcard
        # else:
        #     return None  # draw
        for i, opposingcard in enumerate(opposing.raw):
            if Card(self.raw[i]) != Card(opposingcard):
                return Card(self.raw[i]) > Card(opposingcard)

    def __str__(self):
        return f"<{self.raw} -> {self.hand}>"

    def __repr__(self):
        return f"<{self.raw} -> {self.hand}>"

    def __gt__(self, opposing):
        if self.power > opposing.power:
            return True
        elif self.power == opposing.power:
            return self.compare_highest(opposing)
        else:
            return False


def part1(data):
    logger.info("Part 1 start")

    hands = {PokerHand(line.strip().split(" ")[0]): int(line.strip().split(" ")[1]) for line in data}
    total_sum = sum(hands[hand] * (index + 1) for index, hand in enumerate(sorted(hands)))
    logger.debug("Part 1 end")
    return total_sum


def part2(data):
    logger.info("Part 2 start")
    logger.debug("Part 2 end")


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

    print(part1(data))
    print(part2(data))
