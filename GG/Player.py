from Skills import skill
from Skills import skillsList

import random

class player:
    def __init__(self,name,attack,defence,vitality,speed,energy,skill1,skill2,skill3,skill4,skill5,skill6):
        self.attack = attack
        self.name = name
        self.speed = speed
        self.defence = defence  
        self.vitality = vitality
        self.energy = energy
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        self.skill4 = skill4
        self.skill5 = skill5
        self.skill6 = skill6

sukuna =player("Sukuna",45.0,20.0,300.0,20.0,300.0,skillsList.Dismantle,skillsList.Cleave, skillsList.knifeattack,skillsList.Healingfactor,skillsList.MalevolentShrine, skillsList.FlameArrow)
gojo = player("Gojo",50.0,30.0,300.0,10.0,250.0,skillsList.UnlimitedVoid,skillsList.Blue, skillsList.Red, skillsList.Purple, skillsList.Healingfactor,skillsList.Rest )
def takeDamage(user, receiver, skillUsed):
    r = (random.randint(50,100))
    damagaTaken = user.attack*0.25 + (skillUsed.damage*r)/100 + skillUsed.speed*0.25 -(receiver.defence*0.75 + receiver.speed*0.50)
    if user.energy <= skillUsed.energy:
        damagaTaken= 0
        print("Not enough energy to use "+ skillUsed.name)
    else:
        if damagaTaken <0 : damagaTaken= 0 
        user.energy -= skillUsed.energy
        if skillUsed.type == 4:
            user.vitality += skillUsed.damage
            print (str(user.name) +" healed "+ str(skillUsed.damage)+ " heal points")
        else:
            if skillUsed.type ==5:
                user.energy += skillUsed.damage
                print(str(user.name+" rested"))
            else:
                receiver.vitality -= damagaTaken
                print (str(receiver.name) +" took "+ str(damagaTaken)+ " damage points")

    

    
def status(ply):
   print(str(ply.name)+"      "+str(ply.vitality)+" HP   " +str(ply.energy) +" Energy points")
def useMove(user,receiver):


    unum = random.randint(1,6)
    rnum = random.randint(1,6)
    if unum ==1: skillused = user.skill1
    if unum ==2: skillused = user.skill2
    if unum ==3: skillused = user.skill3
    if unum ==4: skillused = user.skill4
    if unum ==5: skillused = user.skill5
    if unum ==6: skillused = user.skill6

    if rnum==1: counter= receiver.skill1
    if rnum==2: counter= receiver.skill2
    if rnum==3: counter = receiver.skill3
    if rnum==4: counter = receiver.skill4
    if rnum==5: counter = receiver.skill5
    if rnum==6: counter = receiver.skill6
    print(str(user.name) +" uses "+ str(skillused.name) + " Level: "+ str(skillused.level))
    for i in range(0,6):
        if skillused.type == 6:
            if counter.type == 6:
             print("DOMAIN CLASH: " + str(skillused.name)+" against "+ str(counter.name))

            else:
             rnum = random.randint(1,6)
             if rnum==1: counter= receiver.skill1
             if rnum==2: counter= receiver.skill2
             if rnum==3: counter = receiver.skill3
             if rnum==4: counter = receiver.skill4
             if rnum==5: counter = receiver.skill5
             if rnum==6: counter = receiver.skill6
            break
                 

    if skillused.type == 4 or skillused ==5:
        takeDamage(user,receiver,skillused)
        status(user)
        status(receiver)
    else:
        print(str(receiver.name) + " countered with " + str(counter.name)+" Level: "+ str(counter.level))
        if skillused.level >= counter.level :
         print(str(user.name) + " won the clash")
         takeDamage(user,receiver,skillused)
         status(user)
         status(receiver)
         
        else:
         print(str(receiver.name) + " won the clash")
         takeDamage(receiver,user,counter)
         status(user)
         status(receiver)
    
        
   