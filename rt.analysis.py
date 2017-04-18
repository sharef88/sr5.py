#!/usr/bin/python3
import random
from collections import Counter


def roll(count):
    rolls = list()
    r_fury = int()
    percent = False
    if count == 0:
        count = 2
        percent = True
    rolls = [random.randint(0, 9) for _ in range(count)]
    for i in rolls:
        if i > 8:
            r_fury += 1
    if percent:
        result = rolls[0]*10 + rolls[1]
        if not result:
            result = 100
        return result, r_fury
    return rolls, r_fury


def calc_attack(skill, variance, base, pen, qualities = []):
    ''' output dict of attack values'''
    #define the rigeous fury array
    r_fury = [0 for _ in range(5)]

    #roll for attack!
    attack, r_fury[0] = roll(0)

    #how many degrees of SUCK
    degrees = int((skill-attack)/10)

    #shortcircuit if failed
    if degrees < 0:
        return {'attack':0, 'damage':0, 'pen':0, 'degrees': degrees}

    #roll damage Dice
    damage, r_fury[1] = roll(variance)

    #sum it up
    damage = sum(damage +
                 [base] +
                 [random.randint(1, 5)*i for i in r_fury])
    return {'attack':attack, 'damage':damage, 'pen':pen, 'degrees': degrees}


print(calc_attack(60, 1, 5, 5))
