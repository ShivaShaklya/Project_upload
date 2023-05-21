import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation
import threading
import time

'''#
start=time.perf_counter()

def hi(sec,msg):
    print("Starting sleep {}".format(msg))
    time.sleep(sec)
    print("Done sleeping")

t1=threading.Thread(target=hi,args=[2,["Hi","a"]])
t2=threading.Thread(target=hi,args=[2,["hello","b"]])

t1.start()
t2.start()

t1.join()
t2.join()


finish=time.perf_counter()
print(f"finished in {round(finish-start,2)}")'''

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

def V_t(velocity,time):
    ax[0,0].cla()
    ax[0,0].plot(time,velocity)
    ax[0,0].title.set_text("Velocity V/s Time")

def A_t(a,time):
    ax[0,1].cla()
    ax[0,1].plot(time,a)
    ax[0,1].title.set_text("Acceleration V/s Time")

def Al_t(altitude,time):
    ax[1,0].cla()
    ax[1,0].plot(time,altitude)
    ax[1,0].title.set_text("Altitude V/s Time")

def Th_t(thrust,time):
    ax[1,1].cla()
    ax[1,1].plot(time,thrust)
    ax[1,1].title.set_text("Thrust V/s Time")
    
def draw_graph(j):
    #print(j)
    row=next(r)
    time.append(float(row[0]))
    velocity.append(float(row[1]))
    a.append(float(row[2]))
    altitude.append(float(row[3]))
    thrust.append(float(row[4]))
    
    '''#Velocity V/s Time
    V_t(velocity,time)
    #Acceleration V/s Time
    A_t(a,t)
    #Altitude V/s Time
    Al_t(altitude,time)
    #Thrust V/s time
    Th_t(thrust,time)'''

    t1=threading.Thread(target=V_t,args=[velocity,time])
    t2=threading.Thread(target=A_t,args=[a,time])
    t3=threading.Thread(target=Al_t,args=[altitude,time])
    t4=threading.Thread(target=Th_t,args=[thrust,time])

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()

ani=FuncAnimation(fig,draw_graph,interval=100)

plt.show()
 
