from PyQt5 import QtCore, QtGui, QtWidgets,uic
from pyqtgraph import PlotWidget
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread,QObject,pyqtSignal

f=open("FlightSimulatorResults.csv","r")
a=[]
velocity=[]
altitude=[]
thrust=[]
time=[]
r=csv.reader(f)
columns=next(r)

class Ui_MainWindow(object):

        def __init__(self,app):
                self.app=app
                self.ui=uic.loadUi("gui_layout.ui")

                self.ui.VT.setTitle("Velocity V/s Time")
                self.ui.AT.setTitle("Acceleration V/s Time")
                self.ui.AlT.setTitle("Altitude V/s Time")
                self.ui.TT.setTitle("Thrust V/s Time")

                self.ui.Start.clicked.connect(self.plot_A2)
                self.ui.Stop.clicked.connect(self.Pause)
                
                self.ui.show()
                self.run()
                
        def plot_A2(self):
                def update_plot():
                    global row
                    try:
                        row=next(r)
                        time.append(float(row[0]))
                        velocity.append(float(row[1]))
                        a.append(float(row[2]))
                        altitude.append(float(row[3]))
                        thrust.append(float(row[4]))

                        self.refV.setData(time,velocity) 
                        self.refA.setData(time,a) 
                        self.refAl.setData(time,altitude)
                        self.refT.setData(time,thrust)       
                    except:
                        pass

                self.Timer=QtCore.QTimer()
                self.Timer.setInterval(100)
                self.Timer.timeout.connect(update_plot)
                self.Timer.start()

                #Velocity V/s Time
                self.refV=self.ui.VT.plot(time,velocity)
                #Acceleration V/s Time
                self.refA=self.ui.AT.plot(time,a)
                #Altitude V/s Time
                self.refAl=self.ui.AlT.plot(time,altitude)
                #Thrust V/s Time
                self.refT=self.ui.TT.plot(time,thrust)
                
        def Pause(self):
                print(row)
                self.ui.L_time.setText(row[0])
                self.ui.L_velocity.setText(row[1])
                self.ui.L_acceleration.setText(row[2])
                self.ui.L_altitude.setText(row[3])
                self.ui.L_thrust.setText(row[4])
                self.Timer.stop() #PAUSES PLOTTING!!!!!!!!!!!!!!!!!!!!!


        def run(self):
                self.app.exec_()

        ###

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow(app)