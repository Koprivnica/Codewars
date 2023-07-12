"""
Zonk is addictive dice game. In each round player rolls 6 dice. Then (s)he composes combinations from them. Each combination gives
certain points. Then player can take one or more dice combinations to his hand and re-roll remaining dice or save his score. Dice in
player's hand won't be taken into account in subsequent rolls. If no combinations can be composed - situation is called "zonk". Player
thrown zonk loses all points in this round and next player moves. So it's player decision when to reroll and when to stop and save his
score.
Your task is simple - just evaluate current roll and return maximum number of points can be scored from it. If no combinations can be
made - function must return string "Zonk" (without quotes) in dynamically typed languages or Zonk in C.

There are different variations of Zonk. In this kata, we will use most common table of combinations:
Combination	Example roll	Points
Straight (1,2,3,4,5 and 6)	6 3 1 2 5 4	1000 points
Three pairs of any dice	2 2 4 4 1 1	750 points
Three of 1	1 4 1 1	1000 points
Three of 2	2 3 4 2 2	200 points
Three of 3	3 4 3 6 3 2	300 points
Three of 4	4 4 4	400 points
Three of 5	2 5 5 5 4	500 points
Three of 6	6 6 2 6	600 points
Four of a kind	1 1 1 1 4 6	2 × Three-of-a-kind score (in example, 2000 pts)
Five of a kind	5 5 5 4 5 5	3 × Three-of-a-kind score (in example, 1500 pts)
Six of a kind	4 4 4 4 4 4	4 × Three-of-a-kind score (in example, 1600 pts)
Every 1	4 3 1 2 2	100 points
Every 5	5 2 6	50 points

Each die cannot be used in multiple combinations the same time, so three pairs of 2, 3 and 5 will worth you only 750 points (for three
pairs), not 850 (for three pairs and two fives). But you can select multiple combinations, 2 2 2 1 6 will worth you 300 points (200 for
three-of-kind '2' plus 100 for single '1' die)

Examples:
[1,2,3] =>  returns 100 = points from one 1
[3,4,1,1,5] =>  returns 250 = points from two 1 and one 5
[2,3,2,3,3,2] =>  returns 500 = three of 2 + three of 3
[1,1,1,1,1,5] =>  returns 3050 = five 1 + one 5
[2,3,4,3,6,6] =>  returns "Zonk" = no combinations here
[2,2,6,6,2,2] =>  returns 400 = four 2, this cannot be scored as three pairs
[1,3,4,3,4,1] =>  returns 750 = three pairs
[3,3,3,3] =>  returns 600 = four of 3
[1,2,3,4,5] =>  returns 150 = it's not straight

Of course, in real Zonk game it's sometimes not worth to collect all combination from roll. Taking less dice and rerolling more
remaining may be better, but task is just to calculate maximum possible score from current single roll.
"""


def create_dice_dict(input_list):
	output_dict = {}
	for num in input_list:
		output_dict[num] = output_dict.get(num, 0) + 1
	return output_dict

def three_of_kind(dice_value):
	if dice_value == 1:
		return 1000
	return dice_value * 100

def zonk_score(dice_list):
	number_of_dices = len(dice_list)
	dict_of_dices = create_dice_dict(dice_list)
	score = 0
	if len(dict_of_dices) == 6:
		return 1000
	if sum(value == 2 for value in dict_of_dices.values()) == 3:
		return 750
	for key, value in dict_of_dices.items():
		if value == 6:
			score += (4 * three_of_kind(key))
		elif value == 5:
			score += (3 * three_of_kind(key))
		elif value == 4:
			score += (2 * three_of_kind(key))
		elif value == 3:
			score += three_of_kind(key)
		elif value == 2 or value == 1:
			if key == 5:
				score += (50 * value)
			if key == 1:
				score += (100 * value)

	if score:
		return score
	return "Zonk"




print(zonk_score([1,1]))