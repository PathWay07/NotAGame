from Skills import *
from SkillLst import * 
from Player import *
from Test import *
from Miscvariables import SkillsList
import time


def battle(player1 ,player2,r):
    t= random.randint(1,2)
    while player1.vitality >0 and player2.vitality> 0 :
        r+= 1
        t+= 1
        print("Round "+str(r))
        player1.energy +=15
        player2.energy +=15
        if (t % 2 )==0:
            useMove(player1,player2)
        else:
            useMove(player2,player1)
       

        time.sleep(3)
    if player1.vitality > 0:
        winner = player1.name
    else:
        winner = player2.name
    print("After " +str(r)+" rounds , the winner is " +str(winner))

def createSkills():
    global SkillsList
    ski = skill
    ski.name = str(input("Name: "))
    ski.damage = int(input("Damage: "))
    ski.speed = int(input("Speed: "))
    ski.energy = int(input("Energy: "))
    ski.level = int(input("Level: "))
    ski.type = int(input("Type: "))
    SkillsList += str( "\n" + str(ski.name) + " = skill(" + "'"+str(ski.name)+"'," +str(ski.damage) +"," +str(ski.speed) +","+str(ski.energy) +","+str(ski.level) +","+str(ski.type) +")" )
    f = open("SkillLst.py", '+a')

    f.write(str(SkillsList))
 
    



    


def InitBasicSkills():
 f = open("SkillLst.py", '+a')

 f.write(str(SkillsList))
 

