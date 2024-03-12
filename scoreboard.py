from typing import List
from hand import Hand
from rules import Rule


class ScoreBoard:

    def __init__(self):
        self.rules = []
        self.points = []

    # In order to use the ScoreBoard we need to register the rules.
    def register_rules(self, rule: List):
        self.rules.extend(rule)  # To append rules to the list.
        self.points = [0] * len(self.rules)

    # A method to count the number of rules we have.
    def rules_count(self):
        return len(self.rules)

    # Method to return a particular rule.
    def get_rule(self, row: int):
        return self.rules[row]

    # Method to assign points
    def assign_points(self, rule: Rule, hand: Hand):
        row = self.rules.index(rule)
        if self.points[row] > 0:
            raise ValueError("ScoreBoard already saved")
        points = rule.points(hand)
        self.points[row] = points
        return points

    # Method to compute the total number of points
    def total_points(self):
        return sum(self.points)

    # Method to create points overview.
    def create_points_overview(self, hand: Hand = None):
        strs = []
        for idx, rule in enumerate(self.rules):
            points = self.points[idx]
            if hand is not None and points == 0 and rule.points(hand) > 0:
                strs.append(f"{idx + 1}. {rule.name()}: +{rule.points(hand)} points ***")
            else:
                strs.append(f"{idx + 1}. {rule.name()}: {points} points")
        return strs
