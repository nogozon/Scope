#!/usr/bin/python

def ADFK (ut,

file=open("save.txt",'w')


Ax=60/ut
Ay=60/ut
Dx=48/ut
Dy=48/ut
Fx=48/ut
Fy=48/ut
Kx=48/ut
Ky=48/ut

sa1=1800/ut/ut
sa2=3000/ut/ut

sd1=1200/ut/ut
sd2=2000/ut/ut

sf1=300/ut/ut
sf2=1200/ut/ut

sk1=120/ut/ut
sk2=1000/ut/ut



for a1 in range(Ax) :
    for a2 in range(Ay):
    	for d1 in range(Dx):
    		for d2 in range(Dy):
    		 	for k1 in range(Kx):
    				for k2 in range(Ky):	
    					if (a1*a2>sa1) and (a1*a2<sa2) and (d1*d2>sd1) and (d1*d2<sd2) and (k1*k2>sk1) and (k1*k2<sk2) :
    						file.write(str(a1)+" "+str(a2)+" "+str(d1)+" "+str(d2)+" "+str(k1)+" "+str(k2)+" ")
    						file.write(str(a1*a2)+" "+str(d1*d2)+" "+str(k1*k2)+"\n")
    	 
file.close()
    	 