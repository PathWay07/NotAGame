

class skill: 
    def __init__(self,name,damage,speed,energy,level, type):
        self.name = name 
        self.damage = damage 
        self.speed = speed
        self.energy = energy
        self.level = level
        self.type = type

    


class skillsList:
    DivergentFist = skill("Divergent Fist", 50,75,65,6,1)
    FireTornado =skill("Fire Tornado",70,25,50,5,2)
    Swordswing = skill("Sword Swing",30,40,15,3,1)
    Charge = skill(" Charge",40,25,15,3,1)
    Skullcrusher = skill("Skullcrusher",20,25,10,1,1)
    Pinpoint = skill("Pinpoint",40,50,49,3,2)
    knifeattack = skill("Knife Attack",40,25,20,1,1)
    Healingfactor = skill("Heal",50,10,50,3,4)
    blastattack = skill("Blast Attack", 50,25,30,2,2)
    Gatlingattack = skill("Gatling Attack",40,30,30,4,3)
    Atomizer = skill("Atomize",30,30,20,3,2)
    BlackFlash = skill("BlackFlash",50,50,50,7,1)
    Red = skill("Red",50,20,50,5,3)
    Blue = skill("Blue",50,30,50,3,3)
    Purple = skill("HOLLOW PURPLE", 150,50,75,7,2)
    Rest = skill("Rest",20,1,0,1,5)
    Dismantle = skill("Dismantle", 50,50,30,7,2)
    Cleave = skill("Cleave", 60,50,40,5,2)
    FlameArrow = skill("Flame Arrow", 100,50,50,6,2)
    UnlimitedVoid = skill("DOMAIN EXPANSION:UNLIMITED VOID",200,100,150,10,6)
    MalevolentShrine = skill("DOMAIN EXPANSION:MALEVOLENT SHRINE",200,100,150,10,6)


class effects:
    def __init__(self,name,damage,duration) -> None:
        self.name = name
        self.damage = damage
        self.duration = duration

class  effectsList:
    Normal = effects("Normal",0,0)
    burning = effects("Burning", 15,3)
    bleeding = effects("Bleeding",10,5)
