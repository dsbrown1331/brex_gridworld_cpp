import numpy as np
import matplotlib.pyplot as plt
from numpy import nan, inf

#Code to evaluate the performance of Bayesian REX vs. Bayesian IRL when both get suboptimal ranked demos and when we use 
# Bayesian IRL from critiques (https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8460854) a method that can learn from good and bad demonstrations.

#This script will compile data for Table 9 in https://arxiv.org/pdf/2002.09089.pdf

sample_flag = 4
chain_length = 5000
step = 0.01
alpha = 50
size = 9
num_reps = 100
rolloutLength = 20
numDemo = 20
top_ks = [0.05, 0.1, 0.25, 0.5]
stochastic = 0



filePath = "data/brex_gridworld_ranked_goodbad/"



birl_ave_plosses = []
brex_ave_plosses = []

for top_k in top_ks:  
    birl_plosses = []
    brex_plosses = []
    if top_k == 0.25 or top_k == 0.05:
        padding = '0000'
    else:
        padding = '00000'
    filename = "GridWorldInfHorizon_numdemos" + str(numDemo) + "_alpha" + str(alpha) + "_chain" + str(chain_length) + "_step" + str(step) + "0000_L1sampleflag" + str(sample_flag) + "_rolloutLength" + str(rolloutLength) + "_stochastic" + str(stochastic) + "_topk" + str(top_k) + padding + ".txt"
    print(filename)
    f = open(filePath + filename,'r')   
    f.readline()                                #clear out comment from buffer
    for line in f:
        items = line.strip().split(",")
        birl_ploss = float(items[0])
        brex_ploss = float(items[1])

        birl_plosses.append(birl_ploss)
        brex_plosses.append(brex_ploss)
    birl_ave_plosses.append(np.mean(birl_plosses))
    brex_ave_plosses.append(np.mean(brex_plosses))

print("Critique Bayesian IRL vs. Suboptimal Ranked Bayesian REX")
for i,d in enumerate(top_ks):
    print("Demos = 20 top/bottom% = {}, BIRL Ploss = {:.3f}  BREX Ploss {:.3f}".format(d*100, birl_ave_plosses[i], brex_ave_plosses[i]))

#print out as a table
print("Table")
print("percentage of ranked demos to use as good/bad")
print_str = ""
for i,d in enumerate(top_ks):
        print_str += "& {}".format(d)
print(print_str + "\\\\")



print_str = ""
print_str += "B-IRL "
for i,d in enumerate(top_ks):
        print_str += "& {:.3f}".format(birl_ave_plosses[i])
print(print_str + "\\\\")

print_str = ""
print_str += "B-REX "
for i,d in enumerate(top_ks):
        print_str += "& {:.3f}".format(brex_ave_plosses[i])
print(print_str + "\\\\")

