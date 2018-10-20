# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:16:21 2018

@author: Alan Jerry Pan, CPA, CSC
@affiliation: Shanghai Jiaotong University

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Profit-Sentient Electronic Bartering Platform [Computer software]. Github repository <https://github.com/alanjpan/Profit-Sentient-Electronic-Bartering-Platform>

Note this software's license is GNU GPLv3.
"""

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
                    supply.remove(i)
                    demand.remove(j)
                    print("sale: " + str(collect))
    print("end cash: " + str(cash))