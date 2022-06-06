# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moabid <moabid@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/05 23:22:28 by moabid            #+#    #+#              #
#    Updated: 2022/06/06 13:31:18 by moabid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import readline
import sys

def	html_generator():
	strTable = '<!DOCTYPE html><html lang="en"><head><title>Periodic Table</title><meta charset="UTF-8"> \
	</head><body><table><tr>'
	
	with open("periodic_table.txt", 'r') as f:
		lines = f.readlines()
		
		for line in lines:
			strTable += '<td style="border: 1px solid black; padding:10px">'
			
			first = line.split(' ')
			first_word = first[0]
			strTable += '<h4>' + first_word + '</h4>'
			
			second = line.split(',')
			second_word = second[0].split(':')
			strTable += '<ul><li>' + second_word[1] + '</li>'
	
			third_word = second[2].split(':')
			strTable += '<li>' + third_word[1] + '</li>'
	
			forth_word = second[3].split(':')
			strTable += '<li>' + forth_word[1] + '</li>'

			fifth_word = second[4].split(':')
			strTable += '<li> Electrons ' + fifth_word[1] + '</li></ul><br>'

	strTable += "</tr></table></body></html>"
	
	hs = open("periodic.html", 'w')
	hs.write(strTable)

if __name__ == '__main__':
	html_generator()