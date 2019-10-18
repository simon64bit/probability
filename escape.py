#******************************************************************************
# escape.py
#******************************************************************************
# Name: Simon Mei
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):NONE
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import random
n= 100000
rs = 0
rs1= 0 

x1 = 0
y1 = 0.2

x2 = 0.2
y2 = 0

x3 = 1
y3 = 1
for i in range(n):
    x  = random.random()
    y  = random.random()
    d1 = ((x - x1)**2 + (y - y1) **2) **0.5
    d2 = ((x - x2)**2 + (y - y2) **2) **0.5
    d3 = ((x - x3)**2 + (y - y3) **2) **0.5
    if d1 <= d2 and d1 <= d3:
        d = d1
    if d2 <= d1 and d2 <= d3:
        d = d2
    if d3 <= d1 and d3 <= d2:
        d = d3
    
    if d < 0.4:
        rs += 1
    rs1+=d
    
        
print('Mean distance =',rs1/n)
print('P(d<0.4)      =',rs/n)
    
