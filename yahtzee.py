import random
# Game description https://en.wikipedia.org/wiki/Yahtzee
# version 0.0.1  player names, 5 dice only sum of points without combos

def main():
	number_of_players = int(input('Enter the number of players (1-6): '))
	print(f'There are {number_of_players} players in this game!')
	if number_of_players > 6:
		print(f'the number of players {number_of_players} has exceeded the maximum (maximum 6)')
	elif number_of_players >0:
		players_names = []
		for i in range(0,number_of_players):
			players_names.append(str(input(f'Enter the name of player number {i}: ')))
		print("Player list: ", str(players_names))
		players_stats = {}
		roll_totals = {}
		dice_rolls = 5
		dice_size = 6
		dice_sum = 0
		for player in players_names:
			players_stats[player] =[]
			for p in range(0,dice_rolls):
				roll = random.randint(1,dice_size)
				dice_sum+=roll
				players_stats[player].append(roll)
				print(f'Die number {p} rolled a {roll}')
			roll_totals[player]=dice_sum	
			print(f'{player} has rolled a total of {dice_sum}')
		print("Roll Totals: ", str(roll_totals))

	else:	
		print(f'unknown number of players {number_of_players}, enter a number from 1 to 6')


if __name__== "__main__":
	main()