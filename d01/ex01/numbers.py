# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moabid <moabid@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/05 17:52:15 by moabid            #+#    #+#              #
#    Updated: 2022/06/05 18:11:53 by moabid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def reader():
	with open("numbers.txt", "r") as file:
		numbers = file.read().split(",")
		for elem in numbers:
			print(elem.strip())

if __name__ == "__main__" :
	reader()