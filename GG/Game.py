from Player import useMove
from Player import gojo
from Player import sukuna
from Player import player
from Skills import skillsList
import time
import random


def battle(player1 ,player2):
    round= 0
    t= random.randint(1,2)
    while player1.vitality >0 and player2.vitality> 0 :
        round+= 1
        t+= 1
        print("Round "+str(round))
        player1.energy +=15
        player2.energy +=15
        if (t % 2 )==0:
            useMove(player1,player2)
        else:
            useMove(player2,player1)
       

        time.sleep(10)
    if player1.vitality > 0:
        winner = player1.name
    else:
        winner = player2.name
    print("After " +str(round)+" rounds , the winner is " +str(winner))

yuji = player("Yuji",75,40,200,75,100,skillsList.BlackFlash, skillsList.DivergentFist,skillsList.Skullcrusher,skillsList.Charge,skillsList.Cleave,skillsList.blastattack)
knight= player("Knight",50,40,100,35,100,skillsList.Swordswing,skillsList.Atomizer,skillsList.Rest,skillsList.Charge,skillsList.blastattack,skillsList.BlackFlash)      
battle(yuji, knight)