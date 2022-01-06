#!usr/bin/env python3
#Dictionary
nations = {
	'Easy' : {
		'Units' : {
			'Cavalry' : 'French',
			'Archery' : 'English'
		},
		'Playstyle' : {
			'Keeps' : 'French',
			'Defense' : 'English',
		}
	},
	'Medium' : {
		'Units' : {
			'Camels':'Abbasid Dynasty',
			'Cavalry':'Rus',
			'Infantry':'Holy Roman Empire',

		},
		'Playstyle' : {
			'Technology' : 'Abbasid Dynasty',
			'Expansion' : 'Rus',
			'Defense' : 'Holy Roman Empire'
		}
	},
	'Hard' : {
		'Units' : {
			'Cavalry': 'Mongols',
			'Elephants' : 'Delhi Sultanate',
			'Gunpowder' : 'Chinese',

		},
		'Playstyle' : {
			'Aggressive': 'Mongols',
			'Research': 'Delhi Sultanate',
			'Dynastics': 'Chinese'
		}
	},

	'Rus' : {
		'Background': 'The Rus derive great benefit from the countryside. They are able to gather resources more readily from hunting and forestry and can field strong combat units. Enemies face strong early game fortifications and a diverse economy that cannot be easily disrupted.',
		'Special Units': ['Warrior Monk', 'Horse Archer', 'The Streltsy'],
		'Flag Color' : 'Red'
    },
	'Holy Roman Empire' : {
		'Background' : 'Prelates enhance the economy of the Holy Roman Empire, while powerful infantry units form the core of its military. Enemies must face an opponent able to rapidly recover from attacks and field strong counterattacks.',
		'Special Units' :['The Prelate','Landsknecht'],
		'Flag Color' : 'Yellow'
    },
	'Delhi Sultanate' : {
		'Background' : 'The Delhi Sultanate stays many steps ahead of their enemies with great networks of scholars. Fully realized, they field the intimidating War Elephant and trample those in their path.',
		'Special Units' : ['The scholar','War Elephant','Tower War Elephant'],
		'Flag Color' : 'Green'
    },
	'Mongols' : {
		'Background' : 'Masters of mobility and mounted warfare, the Mongols can easily relocate their camps. They gain economic benefits from setting up near stone outcroppings and from raiding enemy buildings. Enemies must deal with cavalry attacks from the opening moments of play.',
		'Special Units' : ['The Khan','The Mangudai'],
		'Flag Color' : 'Blue'
	},
	'Chinese' : {
		'Background' : 'The Chinese can shift their focus across the ages, deploying many unique units and building rapidly. Enemies must continually adapt if they want to keep up.',
		'Special Units' : ['The Imperial Official','Fire Lancer','Nest of Bees'],
		'Flag Color' : 'Red'
	},
	'Abbasid Dynasty' : {
		'Background' : 'The Abbasid Dynasty pursues a flourishing Golden Age by concentrating structures around their House of Wisdom, allowing them to unlock significant economic advantages. The House of Wisdom also drives progress through the Ages and grants access to advanced technology. Abbasid camel units are expert at countering enemy cavalry.',
		'Special Units' : ['Camel Archers','Imam'],
		'Flag Color' : 'Black'
	},
	'English' : {
	    'Background' : 'Exceptional early infantry provide the English with a powerful punch backed up by reliable food production from the fields.',
	    'Special Units' : ['The Villager','The Longbowman','The Man-at-Arms'],
		'Flag Color' : 'Red'
	},
	'French' : {
		'Background' : 'The French deploy powerful cavalry units and can boost production in fortified positions. Enemies must be prepared to withstand the charges of powerful Royal Knights and other armored units.',
		'Special Units' : ['The Royal Knight', 'The Arbaletrier', 'The Cannon'],
		'Flag Color' : 'Blue'
    }
}

# Project requirements
# Return unique answers based on the input provided... multiple results should be possible.
# AS BEST YOU'RE ABLE, control for user errors (suggested: methods, try/except, while loop)
# Use at least one while loop.
# Make all code "your own."

# Robert Spring
#Written in python 3.8.5 64 bit (base:conda)
#Which age of empires nation are you?


# Welcome user
print("Hello, welcome to the Age of Empires nation selector!\nWe'll ask a couple questions to find a nation that best suits you.")

# User selects difficulty
# Added last minute flavor, code got janky as a result
print("What's your experience level? (Noob, Meatshield, Cthulhu): .\n")
difficulty = ""
while difficulty != 'Easy' and difficulty != 'Medium' and difficulty != 'Hard':
	difficulty = input("Select your experience level: ").capitalize()
	if difficulty == 'Noob':
		print("Likes the way buildings look in current age, doesn't advance.\n")
		difficulty = "Easy"
	elif difficulty == 'Meatshield':
		print("Every moment I live... is agony.\n")
		difficulty = "Medium"
	elif difficulty == 'Cthulhu':
		print("Sees the people, destroys the people.\n")
		difficulty = "Hard"
	else:
		print("Incorrect input... try again.")

#Player decides to eitehr select nation based off of preferred units or playstyle
player_decision = ''
while player_decision != 'Units' and player_decision != 'Playstyle':
	player_decision = input("Please filter by units or playstyle: ").capitalize()
	if player_decision == 'Units':
		print("A wise choice Táctico\n")
	elif player_decision == 'Playstyle':
		print("Welcome back Strategos.\n")
	else:
		print("Invalid input, try again.")

# Appending either unit or playstyle types into a list for ease of use.
player_final_choices = []
for key in nations[f'{difficulty}'][f'{player_decision}']:
	player_final_choices.append(key)

#Player is assigned nation based on their final choice
#I had to account for difficulty levels that had either two or three civilizations.
final_choice = ''
while final_choice not in player_final_choices:
	if len(player_final_choices) == 2:
		final_choice = input(f"Please select {player_final_choices[0].lower()} or {player_final_choices[1].lower()}: ").capitalize()
		if final_choice == player_final_choices[0]:
			print(f"You selected {player_final_choices[0].lower()}!\n")
		elif final_choice == player_final_choices[1]:
			print(f"You selected {player_final_choices[1].lower()}!\n")
		else:
			print("Incorrect input, try again.")
	elif len(player_final_choices) == 3:
		final_choice = input(f"Please select {player_final_choices[0].lower()}, {player_final_choices[1].lower()} or {player_final_choices[2].lower()}: ").capitalize()
		if final_choice == player_final_choices[0]:
			print(f"You selected {player_final_choices[0].lower()}!\n")
		elif final_choice == player_final_choices[1]:
			print(f"You selected {player_final_choices[1].lower()}!\n")
		elif final_choice == player_final_choices[2]:
			print(f"You selected {player_final_choices[2].lower()}!\n")
		else:
			print("Incorrect input, try again.")

#Informs player of the nation they've selected
selected_nation = nations[f'{difficulty}'][f'{player_decision}'][f'{final_choice}']
print(f"You are the {selected_nation}!")
selected_nation_details = []

#extracts flavor content from dictionary and appends it to a list.
for value in nations[selected_nation].values():
	selected_nation_details.append(value)


# Assigns the contents of this list to a list for readability, considering removing it
special_units = selected_nation_details[1]

#Prints flavor text to user.
print(f"Background: {selected_nation_details[0]}")
if len(special_units) == 2:
	print(f"{special_units[0]}, {special_units[1]}")
elif len(special_units) == 3:
	print(f"Special Units: {special_units[0]}, {special_units[1]}, and {special_units[2]}.")
else:
	print("Warning: Invalid number of units")
print(f"Flag Color: {selected_nation_details[2]}.\n")
