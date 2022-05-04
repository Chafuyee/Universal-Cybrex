"""
Title: The Meed Universe


"""
import random
import math

def main():
    empty = "testing"
    meed_list = initialise_population()

def full_cycle(meed_list):

def single_night(meed_list):

    male_meeds = []
    female_meeds = []

    for meed in meed_list:
        if meed[4] == "F":
            female_meeds += [meed]
        elif meed[4] == "M":
            male_meeds += [meed]
    
    for meed in female_meeds:
        base_chance = 33
        strength = meed[5]
        if strength > 30:
            chance_multiplier = (strength * 0.025)
        else:
            chance_multiplier = 1
        
        birth_chance = round(base_chance * chance_multiplier, 3)
        meed.append(birth_chance)


def single_day():


def initialise_population():

    meed_list = []
    female_names = open("FemaleNames.txt", "r")
    male_names = open("MaleNames.txt", "r")
    male_names_str = male_names.read()
    female_names_str = female_names.read()
    male_names_list = male_names_str.split("\n")
    female_names_list = female_names_str.split("\n")
    meed_start = 10
    is_male = True

    for meed in range(meed_start):

        age = 0
        strength = random.randrange(20,51)
        energy = 100
        energy_cap = 100 + (0.5 * strength)
        attractiveness = random.randrange(1, 101)
        
        name_roll = random.randrange(0, 1200)
        last_baby = None
        offspring_count = 0
        x_pos = round(random.uniform(-400, 400), 3)
        y_pos = round(random.uniform(-400, 400), 3)

        if is_male == True:
            sex = "M"
            name = male_names_list[name_roll]
            is_male = False
        else:
            sex = "F"
            name = female_names_list[name_roll]
            is_male = True
        
        single_meed = [name, x_pos, y_pos, age, sex, strength, energy, energy_cap, attractiveness, last_baby, offspring_count]
        meed_list += [single_meed]

    return meed_list


    
    
initialise_population()