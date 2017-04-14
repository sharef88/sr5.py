#!/usr/bin/python3
'''
Module for the definition of an SR5 character
'''
import json


class Character(object):
    '''
    Character Definition for SR5
    '''
    attributes_ref = ('body', 'agility', 'reaction', 'strength',
                      'willpower', 'logic', 'intuition', 'charisma',
                      'essence')
    active_skill_ref = json.load(open('./skills.json'))

    def __init__(self, **kwargs):
        #set up the valid attribute/skill options
        groups = set([obj['group'] for obj in self.active_skill_ref.values()])
        groups.discard('no')
        #if a value is not in this list, it is invalid, the validation for this will be used later
        valid = self.attributes_ref + tuple(self.active_skill_ref.keys()) + tuple(groups)

        #transpose the skill list to groups
        group_skills = {key: [] for key in groups}
        for key, obj in self.active_skill_ref.items():
            grp = obj['group']
            if not grp == 'no':
                group_skills[grp].append(key)


        self.data = {
            'attributes':  dict(zip(self.attributes_ref, '')),
            'active_skills': dict(zip(self.active_skill_ref, '')),
            'knowledge': dict(),
            'languages': dict(),
        }

        #simple parse of kwargs
        for key in kwargs:
            if key in valid:
                if key in self.attributes_ref:
                    self.data['attributes'][key] = kwargs[key]
                elif key in groups:
                    for key2 in group_skills[key]:
                        self.data['active_skills'][key2] = kwargs[key]
                elif key in self.active_skill_ref:
                    if key in self.data['active_skills'].keys():
                        self.data['active_skills'][key] += kwargs[key]
                    else:
                        self.data['active_skills'][key] = kwargs[key]
                else:
                    raise TypeError('what is %s and what is it doing here?' % key)
            else:
                raise TypeError('attribute/skill "%s" is not in the valid list' % key)

    def attack(self, skill, damage_value, armor_penetration):
        pass
    def defend(self, advanced=None):
        pass
    def resist(self, style):
        pass

test=Character(agility=4, logic=5, pistols=5, sorcery=4)
print(json.dumps(test.data, indent=4))

