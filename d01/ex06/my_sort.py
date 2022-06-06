# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_sort.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moabid <moabid@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/05 23:13:54 by moabid            #+#    #+#              #
#    Updated: 2022/06/05 23:21:57 by moabid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ast import Lambda


def	sorting_dic():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	a = sorted(d.items(), key=lambda x: x[1])
	for value in a:
		print(value[0])
	print("----------")
	a = sorted(d.items(), key=lambda x: x[0])
	for value in a:
		print(value[0])

if __name__ == '__main__':
	sorting_dic()