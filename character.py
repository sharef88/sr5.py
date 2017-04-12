#!/usr/bin/python3
'''
Module for the definition of an SR5 character
'''

class Character(object):
    def __init__(self, *initial_data, **kwargs):
        for obj in initial_data:
            for key in obj:
                setattr(self, key, obj[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
