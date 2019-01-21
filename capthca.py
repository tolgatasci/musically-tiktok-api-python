from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import math



class capthca():
    datam = None
    root = None
    win = None

    backdata = None
    def __init__(self,data):
        self.root = Tk()
        self.win = Canvas(self.root, width=255, height=255)
        self.win.grid()
        self.datam = data
        self.display_image()
        self.display_the_query()

        mainloop()

    def close_window(self):
        # root.destroy()
        self.root.destroy()
    def onclick(self):
        print("You clicked the button")
    def display_image(self):

        img =  PhotoImage(data=self.datam)
        self.win.create_image(70, 200, anchor=NW, image=img)
        label = Label(image=img)
        label.image = img  # keep a reference!


        #rectangle_back = win.create_rectangle(555, 200, 300, 300, fill="gray")



    def display_the_query(self):
        query_label = Label(self.root,
                        text="Enter Captcha Code: ")
        query_entry = Entry(self.root)
        # to be able to track the entry text
        # . notation to attach it as an attribute
        query_entry.var = StringVar()
        '''
             Label(self.root, text="Enter your name:").pack(side=TOP)
              ent = Entry(self.root)
              ent.bind("<Return>", (lambda event: self.okey(ent.get())))
              ent.pack(side=TOP)
              btn = Button(self.root, text="Submit", command=(lambda: self.okey(ent.get())))
              btn.pack(side=LEFT)
             '''
        # to attaching the attribute as the displayed text
        query_entry['textvariable'] = query_entry.var
        result_label = Label(self.root)
        # to actually track the input each time there's a difference
        # which essentially allows dynamically calculating the result

        query_entry.bind("<Return>", (lambda event: self.okey(query_entry.var)))
        query_label.grid()
        query_entry.grid()
        result_label.grid()

    def okey(self,var):
        user_input = var.get()
        if user_input:
            self.backdata = user_input
        self.close_window()
