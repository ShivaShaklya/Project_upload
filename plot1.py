import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation
'''
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("My first graph")
plt.show()
#
f=open("travel_times.csv","r")
r=csv.reader(f)
columns=next(r)
l=[]
for i in r:
    l.append(i[3])
print("Distances: ",l)
#Distance Vs Time Graph
f=open("abc.csv","r")
distance=[]
speed=[]
a=[]
time=[]
e=[]
r=csv.reader(f)
columns=next(r)
for i in r:
    distance.append(float(i[1]))
    speed.append(float(i[2]))
    time.append(int(i[0]))
    a.append(float(i[4]))
    e.append(int(i[3]))
    
fig,ax=plt.subplots(2,2)
#Speed V/s Time
ax[0,0].plot(time,speed,marker="o",markerfacecolor="#DB0F27")
ax[0,0].title.set_text("Speed V/s Time")
#Distance V/s Time
ax[0,1].plot(time,distance,marker="o",markerfacecolor="orange")
ax[0,1].title.set_text("Distance V/s Time")
#Acceleration V/s Time
ax[1,0].plot(time,a,marker="o",markerfacecolor="yellow")
ax[1,0].title.set_text("Acceleration V/s Time")
#Exhaust V/s time
ax[1,1].plot(time,e,marker="o",markerfacecolor="green")
ax[1,1].title.set_text("Exhaust speed V/s Time")
plt.show()
##
f=open("flightSimulatorResults.csv","r")
velocity=[]
altitude=[]
a=[]
time=[]
thrust=[]
r=csv.reader(f)
columns=next(r)
for i in r:
    time.append(float(i[0]))
    velocity.append(float(i[1]))
    a.append(float(i[2]))
    altitude.append(float(i[3]))
    thrust.append(float(i[4]))
   
fig,ax=plt.subplots(2,2)
#Velocity V/s Time
ax[0,0].plot(time,velocity,marker="o",markerfacecolor="#DB0F27")
ax[0,0].title.set_text("Velocity V/s Time")
#Acceleration V/s Time
ax[0,1].plot(time,a,marker="o",markerfacecolor="yellow")
ax[0,1].title.set_text("Acceleration V/s Time")
#Altitude V/s Time
ax[1,0].plot(time,altitude,marker="o",markerfacecolor="orange")
ax[1,0].title.set_text("Altitude V/s Time")
#Thrust V/s time
ax[1,1].plot(time,thrust,marker="o",markerfacecolor="green")
ax[1,1].title.set_text("Thrust V/s Time")
plt.show()'''
#
f=open("flightSimulatorResults.csv","r")
velocity=[]
altitude=[]
a=[]
time=[]
thrust=[]
r=csv.reader(f)
columns=next(r)
fig,ax=plt.subplots(2,2)

def draw_graph(j):
    #print(j)
    '''next(r)
    next(r)
    next(r)
    next(r)'''
    
    row=next(r)
    time.append(float(row[0]))
    velocity.append(float(row[1]))
    a.append(float(row[2]))
    altitude.append(float(row[3]))
    thrust.append(float(row[4]))
    print(time)
    print(velocity)
    print(a)
    print(altitude)
    print(thrust)
    ax[0,0].cla()
    ax[0,1].cla()
    ax[1,0].cla()
    ax[1,1].cla()
    #Velocity V/s Time
    ax[0,0].plot(time,velocity,markerfacecolor="#DB0F27")
    ax[0,0].title.set_text("Velocity V/s Time")
    #Acceleration V/s Time
    ax[0,1].plot(time,a,markerfacecolor="yellow")
    ax[0,1].title.set_text("Acceleration V/s Time")
    #Altitude V/s Time
    ax[1,0].plot(time,altitude,markerfacecolor="orange")
    ax[1,0].title.set_text("Altitude V/s Time")
    #Thrust V/s time
    ax[1,1].plot(time,thrust,markerfacecolor="green")
    ax[1,1].title.set_text("Thrust V/s Time")

ani=FuncAnimation(fig,draw_graph,interval=100)


plt.show()
 

