#IMPORTANT: this is my work in progress attempt at creating a p/pdot graph for pulsars found in the globular cluster NGC104. As of right now it does not produce any plots, as i think my am still lacking in some understanding of how the equations connect to one another.
#Code by M.Thomas
#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#Pulsars within NGC104
pulsar = pd.read_csv['']
#pulsar paramters here

P = [] #Pulsar's period'
T = [] #time of the period

pf = [] #final period
po = [] #start peiord
tf = [] #final time
to = [] #start time

#I may have to do a for loop for each period found with respect to time. something like; for i in time: period(i)... possibly something like that. As i think with my current set up it only looks at a single pulsar periods and #time related not multiple.

def period(p, t):
    return((pf-po)/(tf-to))


Pdot = period(P, T)  #Dervitibe of the Pulsar's period'

print("Pdot") #Works for dummy veribles, so it should work for actual data.

PdotLOG = math.log10('Pdot')

#distance to NGC104. This will be used when plotting the line of best fit.
d_pc = 4450
mu = 5*np.log10(d_pc/10) # d_pc = cluster distance in parsecs

#Age lines
Ages_to_plot = [] #Should use the ages of the GC
Ages_labels = [] #labels for ages

#radio band

#xray band

#errors

#plotting
plt.figure(figsize = (12, 12))
plt.scatter(P, PdotLOG, marker = '*', s=8, label="NGC104_pulsars", color = "black")

