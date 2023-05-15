import matplotlib.pyplot as plt
import csv
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
print("Distances: ",l)'''
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
#plt.title("Distance V/s Time")
#Acceleration V/s Time
ax[1,0].plot(time,a,marker="o",markerfacecolor="yellow")
ax[1,0].title.set_text("Acceleration V/s Time")
#Exhaust V/s time
ax[1,1].plot(time,e,marker="o",markerfacecolor="green")
ax[1,1].title.set_text("Exhaust speed V/s Time")
plt.show()

