#!/usr/bin/python3
'''Building Shadowrun 5 rules into python'''
import random
import json
from collections import Counter
import character

def calculate_hits(dice_pool, limit):
    '''
    calculate the number of 'hits' when rolling a specified dicepool
    dice_pool can be int, or something sum()-able
    '''
    if not isinstance(dice_pool, int):
        dice_pool = sum(dice_pool)
    results = Counter(
        [random.randint(1, 6) for _ in range(dice_pool)]
    )
    hits, glitch = results[6]+results[5], 0
    if hits > limit:
        hits = limit
    if results[1] >= (dice_pool/2):
        glitch = 1
        if not hits:
            glitch = 2
    return (hits, glitch)


def calculate_combat(attacker, defender):
    '''
    calculate the results of combat
    '''
    #initalize the results output-dictionary
    faux_limit = 4
    results = {}

    #PHASE 1 roll initial attack
    first_hits = {
        'attacker':calculate_hits(attacker.skill + attacker.attribute, faux_limit),
        'defender':calculate_hits(defender.intuition + defender.reaction, faux_limit)
        }
    first_net = first_hits['attacker'][0] - first_hits['defender'][0]

    #PHASE 2 determine damage type
    damage_type = 'P'
    if (first_net + attacker.dv)\
        < (defender.armor - attacker.ap):
        damage_type = 'S'

    #PHASE 3 body_resist
    body_resist = calculate_hits(defender.body + defender.armor - attacker.ap, faux_limit)

    #calculate damage, accounting for the body-resist
    results['damage'] = [first_net + attacker.dv - body_resist[0], damage_type]

    #null the damage if the value is < 0
    if results['damage'][0] < 0:
        results['damage'][0] = 0

    #build the glitch output, just in case
    results['glitch'] = {
        'attack':first_hits['attacker'][1],
        'defense':first_hits['defender'][1],
        'resist':body_resist[1]
        }

    if first_net < 1:
        results['damage'][0] = 0
    #finalize the damage value as a tuple (easier to use for calculations)
    results['damage'] = tuple(results['damage'])

    #the thing, has been done
    return results

JOHN = character.Character(skill=6, attribute=5, ap=2, dv=2)
SIEN = character.Character(skill=3, attribute=2, ap=0, dv=7)
MOOK = character.Character(intuition=3, reaction=4, body=4, armor=12)

print(
    Counter(
        [
            tuple(
                calculate_combat(defender=MOOK, attacker=SIEN)['damage']
                )
            for _ in range(100)
            ]
    )
)
