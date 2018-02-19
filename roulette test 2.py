#Roulette Simulator
##00,0-36, 38 possibilities
##3 bet types
##    35:1 - single numbers
##    1:1 - even/odd except 0,00
##    2:1 - dozen numbers except 0,00
##ask for starting money, number of spins, bet amount, betting strategy
##stop when spins run out or money runs out
##Output-total spins, total wins/losses, winning/losing percentage, money left, net winnings

from random import randrange


startingCash = float(input("Enter the number of dollars you start with: "))
untouchedCash = startingCash
numSpins = int(input("Enter the number of spins you will play: "))
betAmount = int(input("Enter how many dollars you will bet for each spin: "))


inputStrategy = input(" - Bet on a (s)ingle number (pays 35 to 1) \n - Bet on (e)ven or odd numbers (pays 1 to 1)\n - Bet on a (d)ozen numbers (pays 2 to 1)\n \nEnter your strategy choice (s, e, d): ")

if inputStrategy == "s":
    singleNumber = int(input("Enter the single number you want to bet on (00 or 0 to 36): "))
elif inputStrategy == "e":
    inputStrategy = input("Enter if you want to bet on (e)ven or (o)dd numbers: ")
elif inputStrategy == "d":
     inputStrategy = input("Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36: ")
    
    
gamesWonCount = 0
gamesLostCount = 0
for simulateGame in range(numSpins):
    roll = randrange(-1,37)
    
    if startingCash > 0:
        if inputStrategy == "s" and roll == singleNumber:
            startingCash = startingCash + betAmount * 35
            gamesWonCount = gamesWonCount + 1
        elif inputStrategy == "s" and roll != singleNumber:
            startingCash = startingCash - betAmount
            gamesLostCount = gamesLostCount + 1
        
        elif inputStrategy == "e" and roll %2 == 0:
            startingCash = startingCash + betAmount
            gamesWonCount = gamesWonCount + 1
        elif inputStrategy == "e" and roll %2 != 0:
            startingCash = startingCash - betAmount
            gamesLostCount = gamesLostCount + 1
            
        elif inputStrategy == "o" and roll %2 != 0:
            startingCash = startingCash + betAmount
            gamesWonCount = gamesWonCount + 1
        elif inputStrategy == "o" and roll %2 == 0:
            startingCash = startingCash - betAmount
            gamesLostCount = gamesLostCount + 1

        elif inputStrategy == "1" and roll>=1 and roll<=12:
            startingCash = startingCash + betAmount * 2
            gamesWonCount = gamesWonCount + 1
        elif inputStrategy == "1" and roll>12:
            startingCash = startingCash - betAmount
            gamesLostCount = gamesLostCount + 1
            
        elif inputStrategy == "2" and roll>=13 and roll<=24:
            startingCash = startingCash + betAmount * 2
            gamesWonCount = gamesWonCount + 1
        elif inputStrategy == "2" and roll>=1 and roll<=12:
            startingCash = startingCash - betAmount
            gamesLostCount = gamesLostCount + 1                    
        elif inputStrategy == "2" and roll>=25 and roll<=36:
            startingCash = startingCash - betAmount
            gamesLostCount = gamesLostCount + 1
            
        elif inputStrategy == "3" and roll>=25 and roll<=36:
            startingCash = startingCash + betAmount * 2
            gamesWonCount = gamesWonCount + 1            
            
        elif inputStrategy == "3" and roll<25:
            startingCash = startingCash - betAmount
            gamesLostCount = gamesLostCount + 1            
    else:
         break
winPercentage = (gamesWonCount/numSpins)*100
lossPercentage = (1-(gamesWonCount/numSpins))*100
netCash = startingCash - untouchedCash
totalSpins = gamesWonCount + gamesLostCount

print("After {0} spins".format(totalSpins))
print("Wins: {0} ({1:0.2f}%)".format(gamesWonCount,winPercentage))
print("Losses: {0} ({1:0.2f}%)".format(gamesLostCount,lossPercentage))
print("Ending bank: {0}".format(startingCash))
print("Net winnings: {0}".format(netCash))
            

            
            
            
            
            
            
            
            
            
            