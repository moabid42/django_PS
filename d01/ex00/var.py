# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moabid <moabid@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/05 17:32:30 by moabid            #+#    #+#              #
#    Updated: 2022/06/05 17:50:50 by moabid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def printer(var):
	print("{0} est de type {1}".format(var, type(var)))

def	my_var() :
	printer(42)
	printer("42")
	printer("quarante-deux")
	printer(42.0)
	printer(True)
	printer([42])
	printer({42: 42})
	printer((42, ))
	printer(set())

if __name__ == "__main__":
	my_var()
		
		