# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# from turtle import Turtle, Screen

# jimmy = Turtle()
# print(jimmy)
# jimmy.shape('turtle')
# jimmy.color('coral')
# jimmy.forward(100)
# jimmy.speed(.01)

# turtle_screen = Screen()
# turtle_screen.exitonclick()


from prettytable import PrettyTable
poke_table = PrettyTable()
poke_table.add_column('Pokemon Name', ['Pikachu', 'Squirtle'])
poke_table.add_column('Type', ['Electric', 'Water'])
print(poke_table)
poke_table.add_row(['Charmander', 'Fire'])
print(poke_table)
poke_table.align = 'l'
print(poke_table)
