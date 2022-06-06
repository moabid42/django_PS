# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moabid <moabid@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/05 19:01:22 by moabid            #+#    #+#              #
#    Updated: 2022/06/05 19:31:42 by moabid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def keysearch():
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

	result = "Unknown state"
	if len(sys.argv) != 2:
		sys.exit()
	state = sys.argv[1]
	if state in states:
		abbre = states[state]
		if abbre in capital_cities:
			result = capital_cities[abbre]
	print(result)

if __name__ == '__main__':
	keysearch()