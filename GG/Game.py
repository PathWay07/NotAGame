
from Player import *
from Skills import *
from SkillLst import *
from Miscvariables import roundnum
from InitFiles import * 

import time
import random

    

r = roundnum


j1 = player("J1 ",20,20,100,20,100,knifeattack,Dismantle,DivergentFist,Rest,Swordswing,Healingfactor)
j2 = player("J2 ",20,20,100,20,100,knifeattack,Dismantle,DivergentFist,Rest,Swordswing,Healingfactor)

battle(j1,j2,r)

