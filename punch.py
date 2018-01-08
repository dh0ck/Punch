#!/usr/bin/python3
from tkinter import *
import time, random

ALL=W+E+N+S
class Application(Frame):

    def __init__(self, master=None):
        self.width = '10'
        self.height = '10'

        Frame.__init__(self,master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        
        
        self.rowconfigure(1,weight=1)
        self.columnconfigure(1,weight=1)
        
        frame_0= Frame(self, border=2, relief=RIDGE)
        frame_0a= Frame(self, border=2, relief=RIDGE)
        frame_1= Frame(self, border=2, relief=RIDGE)
        frame_2= Frame(self, border=2, relief=RIDGE)        
        frame_3= Frame(self, border=2, relief=RIDGE)        
        frame_4= Frame(self, border=2, relief=RIDGE)        
        frame_5= Frame(self, border=2, relief=RIDGE)        
        frame_6= Frame(self, border=2, relief=RIDGE)        
        
        frame_0.grid(row=0, column=0, rowspan=1,columnspan=2,sticky=ALL)
        frame_0a.grid(row=1, column=0, rowspan=1,columnspan=2,sticky=ALL) 
        frame_1.grid(row=2, column=0, rowspan=1,columnspan=1,sticky=ALL)
        frame_2.grid(row=2, column=1, rowspan=1,columnspan=1,sticky=ALL)
        frame_3.grid(row=3, column=0, rowspan=1,columnspan=1,sticky=ALL)
        frame_4.grid(row=3, column=1, rowspan=1,columnspan=1,sticky=ALL)
        frame_5.grid(row=4, column=0, rowspan=1,columnspan=1,sticky=ALL)
        frame_6.grid(row=4, column=1, rowspan=1,columnspan=1,sticky=ALL)

        
        self.label_1 = Label(frame_1, bg="white",height=self.height,width=self.width)
        self.label_1.pack(fill="both", expand=True)
        self.label_2 = Label(frame_2, bg="white",height=self.height,width=self.width)
        self.label_2.pack(fill="both", expand=True)
        self.label_3 = Label(frame_3, bg="white",height=self.height,width=self.width)
        self.label_3.pack(fill="both", expand=True)	
        self.label_4 = Label(frame_4, bg="white",height=self.height,width=self.width)
        self.label_4.pack(fill="both", expand=True)
        self.label_5 = Label(frame_5, bg="white",height=self.height,width=self.width)
        self.label_5.pack(fill="both", expand=True)
        self.label_6 = Label(frame_6, bg="white",height=self.height,width=self.width)
        self.label_6.pack(fill="both", expand=True)
        
        var = DoubleVar()
        self.sli = Scale(frame_0, variable=var, orient=HORIZONTAL,from_=1,to=10)
        self.sli.pack(fill="x",expand=False)

        self.but = Button(frame_0a,text='START', command=self.start)
        self.but.pack(fill="x",expand=False)

    def clear(self):
        self.label_1.configure(bg='white')
        self.label_2.configure(bg='white')
        self.label_3.configure(bg='white')
        self.label_4.configure(bg='white')
        self.label_5.configure(bg='white')
        self.label_6.configure(bg='white')
        

    def start(self):
        i=0
        self.clear()
        spd = self.sli.get()

        a = random.randint(0,6)
        b = random.randint(0,1)
        if a == 0:
            print('0')
            if b == 0:
                self.label_1.configure(bg='red')
            else:
                self.label_1.configure(bg='blue')
        elif a == 1:
            print('1')
            if b == 0:
                self.label_2.configure(bg='red')
            else:
                self.label_2.configure(bg='blue')
        elif a == 2:
            print('2')
            if b == 0:
                self.label_3.configure(bg='red')
            else:
                self.label_3.configure(bg='blue') 
        elif a == 3:
            print('3')
            if b == 0:
                self.label_4.configure(bg='red')
            else:
                self.label_4.configure(bg='blue')      
        elif a == 4:
            print('4')
            if b == 0:
                self.label_5.configure(bg='red')
            else:
                self.label_5.configure(bg='blue')  
        elif a == 5:
            print('5')
            if b == 0:
                self.label_6.configure(bg='red')
            else:
                self.label_6.configure(bg='blue')    
        elif a == 6:
            print('6')
            pass 
        delay = (1000-100*int(spd))
        self.after(delay,self.start)
     

root = Tk()
app = Application(master=root)
app.mainloop()
