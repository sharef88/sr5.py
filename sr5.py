#!/usr/bin/python3
'''Building Shadowrun 5 rules into python'''
import random
import json
from collections import Counter
import character

def calculate_hits(dice_pool):
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
    if results[1] >= (dice_pool/2):
        glitch = 1
        if not hits:
            glitch = 2
    return (hits, glitch)

#Attacker = namedtuple('Attacker', 'skill attribute ap dv')
#Defender = namedtuple('Defender', 'intuition reaction body armor')

#JOHN = Attacker(skill=6, attribute=5, ap=2, dv=6)
#MOOK = Defender(intuition=3, reaction=4, body=4, armor=6)

JOHN = character.Character(skill=6, attribute=5, ap=2, dv=6)
MOOK = character.Character(intuition=3, reaction=4, body=4, armor=6)

def calculate_combat(attacker, defender):
    '''
    calculate the results of combat
    '''
    results = {}

    #PHASE 1
    first_hits = {
        'attacker':calculate_hits(attacker.skill + attacker.attribute),
        'defender':calculate_hits(defender.intuition + defender.reaction)
        }
    first_net = first_hits['attacker'][0] - first_hits['defender'][0]

    #results need a glitch notation


    #PHASE 2
    results['damage_type'] = 'P' if first_net + attacker.dv > defender.armor - attacker.ap else 'S'

    #PHASE 3
    body_resist = calculate_hits(defender.body + defender.armor - attacker.ap)
    results['damage'] = first_net + attacker.dv - body_resist[0]

    results['glitch'] = {
        'attack':first_hits['attacker'][1],
        'defense':first_hits['defender'][1],
        'resist':body_resist[1]
        }

    if first_net < 1:
        results = results['glitch']
        return 'defender wins', results
    return 'attacker wins', results


for _ in range(10):
    print(calculate_combat(defender=MOOK, attacker=JOHN))
