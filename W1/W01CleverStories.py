"""
Author: Michael Wiseman
Date: 3/2/2026
"""

# Used \n to make a blank lines instead of print()
# Added .upper() to emphasize the exclamation
#
verb = ["","",""]
print("Please enter the following:\n")
adjective = input("Adjective: ")
animal= input("Animal: ")
verb[0] = input("Verb: ")
exclamation = input("Exclamation: ")
verb[1] = input("Verb: ")
verb[2] = input("Verb: ")


print('\nThe other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb[0]} down the hallway. "{exclamation.upper()}!" I yelled. But all')
print(f'I could think to do was to {verb[1]} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb[2]}')
print('right in front of my family.\n')
