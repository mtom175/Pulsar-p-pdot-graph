#IMPORTANT: this is my work in progress attempt at creating a p/pdot graph for pulsars found in the globular cluster NGC104. As of right now it does produce plots but i am unsure if they are correct, as i think my am still lacking in some understanding of how the equations connect to one another.
#Code by M.Thomas
#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#Pulsars within NGC104
pulsar = pd.read_csv("REPLACE WITH YOUR DATA")
#pulsar paramters here

P = pulsar["PERIOD_(ms)"] #Pulsar's period'
print(P, "as period of pulsars")
Pdot = pulsar["Pdot_(10-20)"] #dervitive of the pulsar
print(Pdot, "as dervitive of the period of pulsars")
#creating a log of the dervitive of the period
PdotLog = []
for i in Pdot:
    Log = np.log(i)
    PdotLog.append(Log)
print(PdotLog, "as the log of Pdot")
#T = [] #time of the period

#pf = [] #final period
#po = [] #start peiord
#tf = [] #final time
#to = [] #start time

#I may have to do a for loop for each period found with respect to time. something like; for i in time: period(i)... possibly something like that. As i think with my current set up it only looks at a single pulsar periods and #time related not multiple.

#def period(p, t):
#    return((pf-po)/(tf-to))


#Pdot = period(P, T)  #Dervitibe of the Pulsar's period'

#print("Pdot") #Works for dummy veribles, so it should work for actual data.

#PdotLOG = math.log10('Pdot')

#distance to NGC104. This will be used when plotting the line of best fit.
d_pc = 4450
mu = 5*np.log10(d_pc/10) # d_pc = cluster distance in parsecs

#Age lines
#Ages_to_plot = [] #Should use the ages of the GC
#Ages_labels = [] #labels for ages

#creating the death line
R = 1 # radius REPLACE with actual radius, to get it to run right now i am using the number one as it does not run with just [] as the placeholder.
c = 3*10**8 #speed of light
I = 1 #REPLACE with actual interia, to get it to run right now i am using the number one as it does not run with just [] as the placeholder.

def B(x, y):
    a = 90 #not sure on the angel just assuming for now
    trig = 1/math.sin(a) #possibly the trig part of the equation? called it trig for the time being due to the sin, will update when i have a better naming system.
    Y = ((3*I*(c**3)**P*Pdot)/2*((math.pi)**2)*(R*6)) #same with this called it Y for the time being and will be updated when i think of a better naming convention.
    return(trig*Y)

#Calling these placeholder as i am not sure what to name them just yet.
placeholder_A= []
placeholder_B = []
Bp = B(placeholder_A, placeholder_B)
print(Bp, "as test") #seemly works, have not tried with the actual P and Pdot data from the csv file, have only tried with dummy veriables

omega = 1 #REPLACE with actual paramter, to get it to run right now i am using the number one as it does not run with just [] as the placeholder.

def Vmax(phi):
    phiMAX = ((Bp)*(R**3)*(omega)**2)/(2*(c**2))
    return(phiMAX)

delV_max = Vmax(placeholder_A)
print(delV_max, "as test 2") #also seemly works, not tried with the actual P and Pdot data from the csv files though.

delV_low = 10**12 #volts... comes from this proceeding https://www.cambridge.org/core/services/aop-cambridge-core/content/view/15615B2A3923506930AC7AFD800FD66F/S1743921317009772a.pdf/div-class-title-equation-of-state-and-pulsar-death-line-div.pdf

#defining the eqiation of state (eos) for the death line
mass = []
inertia = []

#radio band

#xray band

#errors

#plotting
plt.figure(figsize = (12, 12))
plt.title("P/Pdot diagram test")
plt.scatter(P, Pdot, marker = '*', s=5, label="NGC104_pulsars", color = "black")
plt.xlabel("Period(ms)", fontsize = 25)
plt.ylabel("Pdot(10-20)", fontsize = 25)
plt.legend(fontsize = 25)
plt.show()

#Not sure if the P/Pdot diagram LOG test looks correct? but it does plot.
plt.figure(figsize = (12, 12))
plt.title("P/Pdot diagram LOG test")
plt.scatter(P, PdotLog, marker = '*', s=5, label="NGC104_pulsars", color = "black")
plt.xlabel("Period(ms)", fontsize = 25)
plt.ylabel("LogPdot(10-20)", fontsize = 25)
plt.legend(fontsize = 25)
plt.show()

