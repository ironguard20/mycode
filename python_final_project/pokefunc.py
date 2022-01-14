#!/usr/bin/env python3

"""
Author: Robert Spring

This file stores my poke-functions for my battler

"""
import requests
import random
from random import randint
from prettytable import PrettyTable


def battle_damage(attacking_pokemon, defending_pokemon, selected_move):
    """This function takes information from the attacking and
    defendng pokemon and determines the damage output of
    the attacker"""
    attack = attacking_pokemon["moves"][f"{selected_move}"]
    attack_type = attack[0]

    # Absent modifiers, = to the attack or special (depending on whether a physical or special attack is being used) of the attacking pokemon
    if attack_type == "physical":
        a = attacking_pokemon["stats"]["attack"]
    elif attack_type == "special":
        a = attacking_pokemon["stats"]["special-attack"]

    # b = attack Power
    # The power values reported in the attacks section for physical or special attacks being used.
    b = attacking_pokemon["moves"][f"{selected_move}"][2]

    # c = defender's Defense or Special
    # Absent modifiers, = to the defense or special defense of the defending pokemon
    if attack_type == "physical":
        c = defending_pokemon["stats"]["defense"]
    elif attack_type == "special":
        c = defending_pokemon["stats"]["special-defense"]

    damage = round(a * (b / c), 0)
    return damage


def input_filter(prompt):
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print("Sorry, please use a string.")
            continue
        except TypeError:
            print("Sorry, please use a string.")
            continue
        else:
            break
    return value


def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in
    the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


def poke_picker():
    """This function pulls json data from the pokemon api 
    and dynamically parses it for data we need. It then outputs
    that data into a python dictionary to be used by the battler"""
    poke_selector = random.randint(1, 151)
    pokeurl = f"http://pokeapi.co/api/v2/pokemon/{poke_selector}/"
    pokemon = requests.get(f"{pokeurl}")
    pokemon = pokemon.json()
    # print(pokemon)

    # create dict for pokemon
    pokedat = {}

    # collects the pokemon name
    pokedat["name"] = pokemon["name"]

    # collects the pokemon id
    pokedat["id"] = pokemon["id"]

    # colects pokemon sprite link
    pokedat["sprite"] = pokemon["sprites"]["front_default"]

    # loop to collect four pokemon moves - Note: potentially modify to create move db
    # collect damage_class : name from api/v2/move/num/
    moves = {}
    counter = 0
    while counter < 4:
        selector = random.randint(0, (len(pokemon["moves"]) - 1))
        move = pokemon["moves"][selector]["move"]["name"]
        url = pokemon["moves"][selector]["move"]["url"]
        move_getter = requests.get(f"{url}").json()
        move_damage_class = move_getter["damage_class"]["name"]
        move_power = move_getter["power"]
        if move_damage_class != "status" and move_power != None:
            move_type = move_getter["type"]["name"]
            move_power_points = move_getter["pp"]
            move_data = []
            for i in [move_damage_class, move_type, move_power, move_power_points]:
                move_data.append(i)
            moves = add_values_in_dict(moves, f"{move}", move_data)
            counter += 1
        else:
            continue
    pokedat["moves"] = moves
    # loop to collect the six pokemon stats
    stats = {}
    counter = 0
    while counter < len(
        pokemon["stats"]
    ):  # iterates over list and collects base stat names and values
        stats_name = pokemon["stats"][counter]["stat"]["name"]
        stats_value = pokemon["stats"][counter]["base_stat"]
        stats[stats_name] = stats_value
        counter += 1
    pokedat["stats"] = stats

    # Loop to collect pokemon types
    counter = 0
    type_data = []
    while counter < len(pokemon["types"]):
        type_value = pokemon["types"][counter]["type"]["name"]
        type_data.append(type_value)
        counter += 1
    pokedat["types"] = type_data
    # print(f"Name: {name}\nNumber: {number}\nFirst Move: {first_move}\nSecond Move: {second_move}\nThird Move: {third_move}\nFourth Move: {fourth_move}\nSprite: {sprite}\nStats: {stat_name} : {stat_value}")
    # with open('pokemon.json', 'w') as outfile:
    #    json.dump(pokemon, outfile, indent=4)
    return pokedat


def pokebattler(player_name, PokeA, PokeB):
    """This function takes information from the attacking and
    defendng pokemon and determines the damage output of
    the attacker"""
    move_table = PrettyTable()
    poke_table = PrettyTable()
    opponent = "Gary"

    PokeA = poke_picker()
    PokeB = poke_picker()

    PokeA_name = str(PokeA["name"]).capitalize()
    PokeB_name = str(PokeB["name"]).capitalize()
    # Assign HP and add hp buff to extend pokemon life
    hp_buff = 200
    PokeA_hp = PokeA["stats"]["hp"] + hp_buff
    PokeB_hp = PokeB["stats"]["hp"] + hp_buff
    print(f"{player_name}: {PokeA_name}, I choose YOU!\n")
    print(f"{opponent}: {PokeB_name}, I choose YOU!\n")

    while PokeA_hp > 0 and PokeB_hp > 0:
        poke_table.field_names = ["", PokeA_name, "vs.", PokeB_name]
        poke_table.clear_rows()
        poke_table.add_row(["HP", PokeA_hp, "", PokeB_hp])
        print(poke_table)
        move_table.field_names = ["Moves", "Dmg. Type", "Damage"]
        move_table.clear_rows()
        for key in PokeA["moves"]:
            move_table.add_row(
                [key, str(PokeA["moves"][key][0]), str(PokeA["moves"][key][2])]
            )
        print(move_table)
        move = input_filter("Select your move: ")
        try:
            battle_move = PokeA["moves"][f"{move}"]
            damage = battle_damage(PokeA, PokeB, move)
            PokeB_hp = PokeB_hp - damage
            print(
                f"{PokeA_name} attacked {PokeB_name} with {move} and did {int(damage)} damage!\n"
            )
            if PokeB_hp > 0:
                print(f"{opponent}: It's my turn!")
                move = []
                for key in PokeB["moves"]:
                    move.append(key)
                move_pick = randint(0, 3)
                damage = battle_damage(PokeB, PokeA, move[move_pick])
                PokeA_hp = PokeA_hp - damage
                print(
                    f"{PokeB_name} attacked {PokeA_name} with {move[move_pick]} and did {int(damage)} damage!"
                )
                if PokeA_hp <= 0:
                    print(f"{PokeA_name} fainted!")
                    gary_mocking = randint(0, 2)
                    if gary_mocking == 0:
                        print(
                            "Gary: If you showed up on time, you would've seen that I got the best Pokémon from Professor Oak! It pays to have a grandfather in the Pokémon business, doesn't it?"
                        )
                    elif gary_mocking == 1:
                        print(
                            "Gary: Sometimes I wonder why I was cursed with this talent."
                        )
                    else:
                        print(
                            f"Gary: Well, {player_name}, ya snooze ya lose, and you're behind right from the start!"
                        )
                else:
                    continue
            else:
                print(f"player wins")
                continue
        except:
            if PokeA_hp <= 0:
                continue
            else:
                print("You have not selected a move.")
                continue

