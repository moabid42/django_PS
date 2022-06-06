# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moabid <moabid@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/05 19:17:58 by moabid            #+#    #+#              #
#    Updated: 2022/06/05 21:04:11 by moabid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def reverse_dict(d):
	reversed_dict = {key : value for (value, key) in d.items()}
	return reversed_dict

def find_state_by_capital():
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
	if len(sys.argv) != 2:
		sys.exit(1)
	capital_city = sys.argv[1]
	result_str = "Unknown capital city"
	rev_states = reverse_dict(states)
	rev_cities = reverse_dict(capital_cities)
	if capital_city in rev_cities:
		state_abbreviation = rev_cities[capital_city]
		if state_abbreviation in rev_states:
			result_str = rev_states[state_abbreviation]
	print(result_str)

if __name__ == '__main__':
	find_state_by_capital()