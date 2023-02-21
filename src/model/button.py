
"""
A class representing a button object with: 
- name in String
- function to be executed
- icon, optional, in a single String unicode to be compatible with discord.py
when the button was called. Meant to be used by navibot.
"""

class Button:

    def __init__(self, name, function, icon=None):
        self.name = name
        self.function = function
        self.icon = icon

    
