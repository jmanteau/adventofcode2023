from collections import defaultdict

from loguru import logger

# Configure loguru logger
LOGLEVEL = "INFO"
logger.remove()
logger.add(lambda msg: print(msg, end=""), level=LOGLEVEL)  # Change level to control what gets printed


def part1(data):
    totalscore = 0
    for card in data:
        cardname, gameresults = card.split(":")
        _numberplayed, _numberresults = gameresults.split("|")
        numberplayed = set([x.strip() for x in _numberplayed.split(" ") if x.strip()])
        numberresults = set([x.strip() for x in _numberresults.split(" ") if x.strip()])
        winnings = numberplayed.intersection(numberresults)

        if winnings:
            power = len(winnings) - 1
            totalscore += 2**power
    return totalscore


def part2(data):
    nbcards = 0
    cards = {}

    for card in data:
        cardname, gameresults = card.split(":")
        _numberplayed, _numberresults = gameresults.split("|")
        numberplayed = set([x.strip() for x in _numberplayed.split(" ") if x.strip()])
        numberresults = set([x.strip() for x in _numberresults.split(" ") if x.strip()])
        winnings = numberplayed.intersection(numberresults)
        cards[cardname.split(" ")[-1]] = len(winnings)

    total = defaultdict(int)

    for cardnb, nbaddcards in cards.items():
        total[cardnb] += 1
        logger.debug(f"Original Card {cardnb}. Now having {total[cardnb]} of them ")
        for addcard in range(nbaddcards):
            nextcardid = addcard + int(cardnb) + 1
            logger.debug(f"  Winning Add Card {nextcardid}:")
            if nextcardid <= len(cards):
                logger.debug(f"    Adding {total[cardnb]} to total of cards for {nextcardid} id")
                total[str(nextcardid)] += total[cardnb]
            else:
                logger.debug(f"    {nextcardid} is more than the max number of cards {len(cards)}. Not taking into account")

    return sum(total.values())


with open("input.txt") as file:
    data = file.readlines()


rawdata = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# data = [x for x in rawdata.splitlines() if x]


# print(part1(data))
print(part2(data))
