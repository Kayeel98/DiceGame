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
    

player_winnings = 0 
house_dice = random.randint(1,12)
player_dice = random.randint(1,12)
print()


print("MooMoo dice shows ({0})".format(house_dice))
print("	 VERSUS				")	
print("{0} dice shows ({1})".format(name,player_dice))

print()


bet_value = bet
if house_dice > player_dice:
	print("MooMoo wins!, you have lost {0}".format(bet_value))
	player_winnings -= bet_value
elif player_dice > house_dice:
	print("Player wins!, you have won {0}".format(bet_value))
	player_winnings += bet_value
else:
	print("Draw, Nobody wins")
	player_winnings + 0 

player_winnings = int(player_winnings)
print("Your current winnings are {0}".format(player_winnings))

print()

print("Do you wanna play again ?")
print("1. YES")
print("2. NAH ill take the L")

decision = input(int("So what is it gonna be: "))

while decision == 1:
	print("MooMoo dice shows ({0})".format(house_dice))
	print("	 VERSUS				")	
	print("{0} dice shows ({1})".format(name,player_dice))
	
	print()
	
	
	bet_value = bet
	if house_dice > player_dice:
		print("MooMoo wins!, you have lost {0}".format(bet_value))
		player_winnings -= bet_value
	elif player_dice > house_dice:
		print("Player wins!, you have won {0}".format(bet_value))
		player_winnings += bet_value
	else:
		print("Draw, Nobody wins")
		player_winnings + 0 
	
	player_winnings = int(player_winnings)
	print("Your current winnings are {0}".format(player_winnings))
	
	print()
	
	print("Do you wanna play again ?")
	print("1. YES")
	print("2. NAH ill take the L")
	
	decision = input(int("So what is it gonna be: "))
	if decision == 0:
		print("your winning / losing are: {0}".format(player_winnings))
		print("Thanks for playing~!")
		break