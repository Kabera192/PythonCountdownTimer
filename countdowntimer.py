import time
from tkinter import *
from tkinter import messagebox

#The tkinter library is for creating UIs 
#Now let us make the interface

clockInterface = Tk()
clockInterface.geometry("500x500")
clockInterface.title("Countdown Timer")
clockInterface.configure(background='orange')

#create the necessary string variables for hours, mins and secs
hourString = StringVar()
minString = StringVar()
secString = StringVar()

#Give the strings their default values
hourString.set("00")
minString.set("00")
secString.set("00")

#Get the user input
hourTextbox = Entry(clockInterface, width=3, font=("Calibri", 20, ""), textvariable=hourString)
minTextbox = Entry(clockInterface, width=3, font=("Calibri", 20, ""), textvariable=minString)
secTextbox = Entry(clockInterface, width=3, font=("Calibri", 20, ""), textvariable=secString)

#Center the textboxes
hourTextbox.place(x=170, y=180)
minTextbox.place(x=220, y=180)
secTextbox.place(x=270, y=180)

#Create the function that will power the timer!
def runTimer():
    try:
        clockTime = int(hourString.get())*3600 + int(minString.get()) *60 + int(secString.get())
    except:
        print("Try Again!")

    while(clockTime > -1):
        totalMins, totalSecs = divmod(clockTime, 60)
        totalHours = 0

        if(totalMins > 60):
            totalHours, totalMins = divmod(totalMins, 60)
        
        #Here we are setting the output of the textboxes
        hourString.set("{0:2d}".format(totalHours))
        minString.set("{0:2d}".format(totalMins))
        secString.set("{0:2d}".format(totalSecs))

        #Update the timer
        clockInterface.update()
        time.sleep(1) 

        #set the notification for when the timer expires
        if(clockTime == 0):
            messagebox.showinfo("", "Blast Off!!!")
        
        clockTime -= 1

#create the start button for the timer
startButton = Button(clockInterface, text='Start Timer', bd='5', command=runTimer)
startButton.place(relx=0.5, rely=0.5, anchor=CENTER)

clockInterface.mainloop()