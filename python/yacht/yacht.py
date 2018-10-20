from collections import Counter

YACHT = (lambda y: 50 if len(set(y)) == 1 else 0)
ONES = (lambda y: digits(y,1))
TWOS = (lambda y: digits(y,2))
THREES = (lambda y: digits(y,3))
FOURS = (lambda y: digits(y,4))
FIVES = (lambda y: digits(y,5))
SIXES = (lambda y: digits(y,6))
FULL_HOUSE = (lambda y: sum(y) if sorted(Counter(y).values()) == [2,3] else 0)
FOUR_OF_A_KIND = (lambda y: four_of_a_kind(y))
LITTLE_STRAIGHT = (lambda y: 30 if sorted(y) == [1,2,3,4,5] else 0)
BIG_STRAIGHT = (lambda y: 30 if sorted(y) == [2,3,4,5,6] else 0)
CHOICE = sum

def digits(y, digit):
    return digit * y.count(digit)

def four_of_a_kind(y):
    same_four = [dice for dice in set(y) if y.count(dice) >= 4]
    return 4*same_four[0] if len(same_four) > 0 else 0

def score(dice, category):
    return category(dice)
