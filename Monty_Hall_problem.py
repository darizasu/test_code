import argparse
import random

parser = argparse.ArgumentParser(description="This script will execute a defined number of 'iterations' of the Monty Hall problem, 'switching' or not the initial random choice after uncovering one of the empty doors. See https://en.wikipedia.org/wiki/Monty_Hall_problem for more info")
parser.add_argument("iterations", type=int, help="Number of iterations for the Monty Hall problem. Specify an integer value.")
parser.add_argument("-s", "--switching", action="store_true", help="Do you want to switch your initial choice after uncovering one of the empty doors ? By specifying this option, you do")

args = parser.parse_args()

def MontyHall(iterations, switch):
	correct = 0
	incorrect = 0
	for n in range(iterations):
		items = [0, 1, 0]
		random.shuffle(items) # put the car randomly in one of the three doors. The three doors are stored in 'items'.
		firstChoice = items[random.randrange(3)] # select one of the doors.
		items.remove(0) # remove one of the empty doors.
		index = 0
		for position in items: # This loop is intended to get the index position of your firstChoice in the new 'items'.
			if position != firstChoice:
				index += 1
			else:
				break
		if switch: # If you decided to switch the door, here you are assigned the other door.
			if index:
				firstChoice = items[0]
			else:
				firstChoice = items[1]
		else:
			firstChoice = items[index] # If you did not decide to switch, then you are assigned the door of your choice.
		if firstChoice: # You will add 1 to correct if you picked the right door, otherwise add 1 to incorrect.
			correct += 1
		else: 
			incorrect +=1
	if switch:
		print('\n\nAfter {} iterations, you chose the right door {} ({}%) times by switching the initial choice'.format(iterations, correct, round((correct * 100)/ iterations, 2)))
	else:
		print('\n\nAfter {} iterations, you chose the right door {} ({}%) times by not switching the initial choice'.format(iterations, correct, round((correct * 100)/ iterations, 2)))

MontyHall(args.iterations, args.switching)
