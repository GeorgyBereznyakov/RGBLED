from tkinter import *
import tkinter.messagebox
import RPi.GPIO as GPIO
#import time
class MyGUI:
    def __init__(self):
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.setup(11,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        self.my_pwm1 = GPIO.PWM(7,100)
        self.my_pwm2 = GPIO.PWM(11,100)
        self.my_pwm3 = GPIO.PWM(13,100)
        self.my_pwm1.start(0)
        self.my_pwm2.start(0)
        self.my_pwm3.start(0)
        self.myWindow = Tk()
        self.myWindow.geometry("1920x1080+0+0")
        self.myWindow.title("RGB LED GUI")
        
        self.var1 = DoubleVar()
        self.var2 = DoubleVar()
        self.var3 = DoubleVar()
        
        self.scale1 = Scale(self.myWindow, variable=self.var1)
        self.scale1.place(x=50, y=40)
        self.scale2 = Scale(self.myWindow, variable=self.var2)
        self.scale2.place(x=120, y=40)
        self.scale3 = Scale(self.myWindow, variable=self.var3)
        self.scale3.place(x=190, y=40)
        
        self.label1= Label(self.myWindow)
        self.label1.place(x=50,y=150)
        self.label2= Label(self.myWindow)
        self.label2.place(x=140,y=150)
        self.label3= Label(self.myWindow)
        self.label3.place(x=240,y=150)
        
        button = Button(self.myWindow, text="Get Value", command=self.do_this)
        button.place(x=100,y=200)
        self.button1=Button(self.myWindow, text="Power", bg='blue', fg='red', command=self.power)
        self.button1.place(x=200,y=200)
        self.button2=Button(self.myWindow, text="Depower", bg='blue', fg='red', command=self.de_power)
        self.button2.place(x=280,y=200)
        cleanGPIO = Button(self.myWindow, text="Clean before quitting", command=self.clean)
        cleanGPIO.place(x=380,y=200)
        buttonquit = Button(self.myWindow, text="quit", command=self.myWindow.destroy)
        buttonquit.place(x=100,y=250)
        
        mainloop()  
    def do_this(self):
        selection1 = "Red =" +str(self.var1.get())
        selection2 = "Green =" +str(self.var2.get())
        selection3 = "Blue =" +str(self.var3.get())
        self.label1.config(text=selection1)
        self.label2.config(text=selection2)
        self.label3.config(text=selection3)
        
    def power(self):
        self.my_pwm1.ChangeDutyCycle(self.var1.get())
        self.my_pwm2.ChangeDutyCycle(self.var2.get())
        self.my_pwm3.ChangeDutyCycle(self.var3.get())
        
    def de_power(self):
        self.my_pwm1.ChangeDutyCycle(0)
        self.my_pwm2.ChangeDutyCycle(0)
        self.my_pwm3.ChangeDutyCycle(0)
        
    def clean(self):
        GPIO.cleanup()
        tkinter.messagebox.showinfo("Cleaned", "Program is ready to close")
        
my_gui = MyGUI()
