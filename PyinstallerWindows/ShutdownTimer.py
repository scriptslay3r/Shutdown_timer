import tkinter as tk
import tkinter.font as font
import os

class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Shutdown Timer")
        self.state = False
        self.minutes = 3600
        self.seconds = 0

        self.mins = 25
        self.secs = 0
        labelFont = font.Font(family='Helvetica', size=40)
        buttonFont = font.Font(family='Helvetica', size=30)

        self.display = tk.Label(master, textvariable="", font = labelFont)
        self.display.config(text="00:00")
        self.display.pack(fill = 'both')
        self.start_button1 = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start 1 Hour Countdown", font = buttonFont, command=self.start1)
        self.start_button1.pack(fill = 'both', expand = 1)
        self.start_button3 = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start 3 Hour Countdown", font = buttonFont, command=self.start3)
        self.start_button3.pack(fill = 'both', expand = 1)
        self.start_button6 = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start 6 Hour Countdown", font = buttonFont, command=self.start6)
        self.start_button6.pack(fill = 'both', expand = 1)
        self.start_button12 = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start 12 Hour Countdown", font = buttonFont, command=self.start12)
        self.start_button12.pack(fill = 'both', expand = 1)
        self.start_button16 = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start 16 Hour Countdown", font = buttonFont, command=self.start16)
        self.start_button16.pack(fill = 'both', expand = 1)
        self.stop_button = tk.Button(master, bg="Red", activebackground="Dark Red", text="Stop", font = buttonFont, command=self.pause)
        self.stop_button.pack(fill = 'both', expand = 1)

    def countdown(self):

        if self.state == True:

            if (self.mins == 0) and (self.secs == 0):
                self.display.config(text="Done!")
                try:
                    os.system('shutdown /s')
                finally:
                    os.system('shutdown now')
                self.state = False
            else:
                self.display.config(text="%02d:%02d" % (self.mins, self.secs))

                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)

    def start1(self):
        if self.state == False:
            self.state = True
            self.mins = 60
            self.secs = self.seconds
            self.countdown()

    def start3(self):
        if self.state == False:
            self.state = True
            self.mins = 180
            self.secs = self.seconds
            self.countdown()

    def start6(self):
        if self.state == False:
            self.state = True
            self.mins = 360
            self.secs = self.seconds
            self.countdown()


    def start12(self):
        if self.state == False:
            self.state = True
            self.mins = 720
            self.secs = self.seconds
            self.countdown()
    def start16(self):
        if self.state == False:
            self.state = True
            self.mins = 960
            self.secs = self.seconds
            self.countdown()
    def pause(self):
        if self.state == True:
            self.state = False



root = tk.Tk()
my_timer = Timer(root)

root.mainloop()
"{:02} : {:02}".format(10, 0)