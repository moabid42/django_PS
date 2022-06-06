# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moabid <moabid@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/05 21:04:45 by moabid            #+#    #+#              #
#    Updated: 2022/06/05 23:11:44 by moabid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def reverse_dict(d):
	reversed_dict = {key : value for (value, key) in d.items()}
	return reversed_dict

def find_state_by_capital(capital_city):
	states = {
		"Oregon":"OR",
		"Alabama":"AL",
		"New Jersey":"NJ",
		"Colorado":"CO"
	}
	capital_cities = {
		"OR":"Salem",
		"AL":"Montgomery",
		"NJ":"Trenton",
		"CO":"Denver"
	}
	rev_states = reverse_dict(states)
	rev_cities = reverse_dict(capital_cities)
	if capital_city in rev_cities:
		state_abbreviation = rev_cities[capital_city]
		if state_abbreviation in rev_states:
			result_str = rev_states[state_abbreviation]
			return result_str
	return False

def find_capital_by_state(state):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if state in states:
		abbre = states[state]
		if abbre in capital_cities:
			result = capital_cities[abbre]
			return result
	return False

def	find_key_by_value():
	if len(sys.argv) != 2:
		sys.exit(1)
	
	strings = sys.argv[1].split(', ')
	for elem in strings:
		if find_state_by_capital(elem) != False:
			print(elem.strip(), " is a capital of ", find_state_by_capital(elem));
		elif find_capital_by_state(elem) != False:
			print(elem.strip(), " is a state of ", find_capital_by_state(elem));
		else :
			if elem.isspace():
				continue;
			print(elem.strip(), " does not exist.")


if __name__ == '__main__':
	find_key_by_value()