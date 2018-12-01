# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:16:21 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Greedy Electronic Bartering Platform [Computer software]. Github repository <https://github.com/alanjpan/Greedy-Electronic-Bartering-Platform>

Note this software's license is GNU GPLv3.
"""

import random
secure_random = random.SystemRandom()

products = ["A", "B", "C", "D", "E"]
prices = [7, 8, 9, 10, 11, 12, 13]

cash = 0
demand = [("A", 5), ("B", 10), ("C", 15)]
supply = [("A", 3), ("B", 10), ("C", 20)]

def buy(item, price):
    demand.append((item, price))
def sell(item, price):
    supply.append((item, price))
    
def transact():
    global cash
    for i in supply:
        for j in demand:
            if i[0] == j[0]:
                if i[1] < j[1]:
                    collect = j[1] - i[1]
                    cash += collect
                    demand.remove(j)
                    print("sale: " + str(collect))
    supply.clear()
    print("end cash: " + str(cash))
    
def populate(n):
    for i in range(n):
        buy(secure_random.choice(products), secure_random.choice(prices))
        sell(secure_random.choice(products), secure_random.choice(prices))
