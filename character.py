#!/usr/bin/python3
'''
Module for the definition of an SR5 character
'''
import json


class Character(object):
    '''
    Character Definition for SR5
    '''

    def _valid_skills(self):
        self.valid = dict()
        self.valid['attributes_ref'] = ('body', 'agility', 'reaction', 'strength',
                                        'willpower', 'logic', 'intuition', 'charisma',
                                        'essence')
        self.valid['active_skill_ref'] = json.load(
            open('./data/skills.json')
            )
        self.groups = set(
            [obj['group'] for obj in self.valid['active_skill_ref'].values()]
            )
        self.groups.discard('no')

    def _parse_input(self, **kwargs):
        '''
        static method for parsing out and sanity-checking the skill data for the character
        '''
        return NotImplementedError

    def __init__(self, **kwargs):
        self.valid = dict()
        self.groups = set()
        raise NotImplementedError
    def attack(self, skill, damage_value, armor_penetration):
        raise NotImplementedError
    def defend(self, advanced=None):
        raise NotImplementedError
    def resist(self, style):
        raise NotImplementedError


