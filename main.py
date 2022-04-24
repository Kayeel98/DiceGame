import random 


name = input("Insert your name here: ")

print()

print("************ WELCOME!, {0} TO THE MOO MOO CASINO **************".format(name))

print()


try:
	bet = input("Place your bets: ")
	bet = int(bet)
	print()
	print ("You have bet: ${0}".format(bet))
	 

except ValueError:
	print("We only accept dollars here at MOOMOO Casino")
	print("")
	print("Example($ 2)")
	print()
	print ("			The following message is brought to you by")
	print()
	print ("					PRESS RUN TO TRY AGAIN")
	print()
	quit()		

def dice_game(bet):	
	house_dice = random.randint(1,12)
	player_dice = random.randint(1,12)
	print()
	
	
	print("MooMoo dice shows ({0})".format(house_dice))
	print("	 VERSUS				")	
	print("{0} dice shows ({1})".format(name,player_dice))
	
	print()
	player_winnings = 0 
	
	if house_dice > player_dice:
		print("MooMoo wins!, you have lost {0}".format(bet))
		player_winnings -= bet
	elif player_dice > house_dice:
		print("Player wins!, you have won {0}".format(bet))
		player_winnings += bet
	else:
		print("Draw, Nobody wins")
		player_winnings + 0 
	player_winnings = int(player_winnings)
	return player_winnings


print()

win = dice_game(bet)


def accumulated_total(win):
	accwin = 0
	accwin += win
	return accwin



accumulated_total(win)

accumulated = accumulated_total(win)

if accumulated < 0:
	print ("Your balance is: {}".format(accumulated))
	print ("Good luck next time.")
elif accumulated >0:
	print ("Your balance is: {}".format(accumulated))
	print ("Hope to see you soon!")
else:
	print ("Seems like you dont have anything, why not try again?")

print()

print("Try again?")
print("1 for Yes, 2 for No")
user_input = input("Insert here:")

	
