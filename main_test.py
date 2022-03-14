"""Statistical analysis for vaccines in the SIR model including vaccination."""
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros

# 1 hour of time unit
beta = 0.0125


gamma = 1/(30*24)    # Recovery rate 1 in 30 days
D = 730              # Model for D days
dt = 0.1             # 6 min
Nt = int(D*24/dt)    # Compute the corresponding number of hours
s = 1/(24*180)     # Average loss of immunity: 120 days, approximately 4 months
p = 0.001*0.65           # vaccination rate * vaccine protection

t = linspace(0, Nt*dt, Nt+1)
S = zeros(Nt+1)
I = zeros(Nt+1)
R = zeros(Nt+1)
V = zeros(Nt+1)

# Initial condition  ( You put our intial conditions)
S[0] = 999999
I[0] = 1 # initiate infection
R[0] = 0
V[0] = 0



# Euler Forward Equation to solve the differential equations
for k in range(87610):
    N = S[k] + I[k] + R[k] #Keep pop size constant
    S[k+1] = S[k] - dt*beta*S[k]*I[k]/N + dt*s*R[k] 
    I[k+1] = I[k] + dt*beta*S[k]*I[k]/N - dt*gamma*I[k]
    R[k+1] = R[k] + dt*gamma*I[k] - dt*s*R[k]
    loss = int(S[k+1] + R[k+1] + I[k+1]) - \
           int(S[0] + R[0] + I[0])
    
    if loss > 0: # include death
        print('loss: %d'  % loss)

for k in range(87610, Nt):
    N = S[k] + V[k] + I[k] + R[k] #Keep pop size constant
    S[k+1] = S[k] - dt*beta*S[k]*I[k]/N + dt*s*R[k] - dt*p*S[k]
    V[k+1] = V[k] + dt*p*S[k] + dt*p*I[k] + dt*p*R[k]
    I[k+1] = I[k] + dt*beta*S[k]*I[k]/N - dt*gamma*I[k] - dt*p*I[k]
    R[k+1] = R[k] + dt*gamma*I[k] - dt*s*R[k] - dt*p*R[k]
    loss = int(V[k+1] + S[k+1] + R[k+1] + I[k+1]) - \
           int(V[0] + S[0] + R[0] + I[0])
    
    if loss > 0: # include death
        print('loss: %d'  % loss)


fig = plt.figure()
l1, l2, l3, l4 = plt.plot(t, S, t, I, t, R, t, V)
fig.legend((l1, l2, l3, l4), ('S', 'I', 'R', 'V'), 'upper left')
plt.xlabel('hours')
plt.show()
        