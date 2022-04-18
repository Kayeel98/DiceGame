import random 


name = input("Insert your name here: ")

print("************WELCOME!, {0} TO THE MOO MOO CASINO**************".format(name))


try:
	bet = input("Place your bets: ")
	bet = int(bet)
	print()
	print ("You have bet: ${0}".format(bet))
	 

except ValueError:
	print("We only accept dollars here")
	print("")
	print("Example($ 2)")
	print ("			The following message is brought to you by")
	print()
	print ("					PRESS RUN TO TRY AGAIN")
	print()
	quit()		
    

player_winnings = 0 
house_dice = random.randint(1,12)
player_dice = random.randint(1,12)
  
print()

print("House dice shows ({0})".format(house_dice))
print("	 VERSUS				")	
print("Player dice shows ({0})".format(player_dice))

print()

bet_value = bet
if house_dice > player_dice:
	print("House wins!, you have lost {0}".format(bet_value))
	player_winnings += bet
elif player_dice > house_dice:
	print("Player wins!, you have won {0}".format(bet_value))
	player_winnings = player_winnings - bet
else:
	print("Draw, Nobody wins")
	player_winnings + 0 

player_winnings = (int(player_winnings))
print("Your current winnings are {0}".format(player_winnings))
x = -20
print(x)