import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\33[94M'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, attack, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attackLow = attack - 10
        self.attackHigh = attack + 10
        self.magic = magic
        self.df = df
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.attackLow, self.attackHigh)


    def generate_spell_damage(self, i):
        magicLow = self.magic[i]["dmg"] - 5
        magicHigh = self.magic[i]["dmg"] + 5
        return random.randrange(magicLow, magicHigh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        for item in self.actions:
            print(str(i) + ":", item)
            i +=1

    def choose_magic(self):
        i = 1
        for spell in self.magic:
            print(str(i) + ":", spell["name"], ("cost:", str(spell["mp"]) + ")")
            i +=1
