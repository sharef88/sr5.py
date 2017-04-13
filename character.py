#!/usr/bin/python3
'''
Module for the definition of an SR5 character
'''
import json

class Character(object):
    attributes_ref = ('body', 'agility', 'reaction', 'strength',
                      'willpower', 'logic', 'intuition', 'charisma',
                      'essence')
    active_skill_ref = json.load(open('./skills.json'))

    def __init__(self, *initial_data, **kwargs):
        #set up the valid attribute/skill options
        groups = set([obj['group'] for obj in self.active_skill_ref.values()])
        groups.discard('no')
        #if a value is not in this list, it is invalid, the validation for this will be used later
        valid = self.attributes_ref + tuple(self.active_skill_ref.keys()) + tuple(groups)

        for obj in initial_data:
            for key in obj:
                setattr(self, key, obj[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
    def attack(self, skill, damage_value, armor_penetration):
        pass
    def defend(self, advanced=None):
        pass
    def resist(self, style):
        pass

test=Character()

