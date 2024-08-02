from webbrowser import get
import numpy as np
from tkinter import *
import joblib



app = Tk()
model = joblib.load("MLR.joblib")
app.config(background="pink")
app.title("Student Performance Model")
app.geometry("720x1080")

# Intercept
a = model.intercept_.item()

# coefficient
b1 = model.coef_.item(0)

b2= model.coef_.item(1)

b3= model.coef_.item(2)

b4= model.coef_.item(3)

b5= model.coef_.item(4)

# class SomeClass:
#     def __init__(self):
#         self.ent_1 = ...
        
        


def reg():
    
    # get = SomeClass()
    
    x1 = float(ent_1.get())
    x2 = float(ent_2.get())
    x3 = float(ent_3.get())
    x4 = float(ent_4.get())
    x5 = float(ent_5.get())
    
    y = a + (b1*x1) + (b2*x2) +(b3*x3)+ (b4*x4)+ (b5*x5)
    lbl_shw.config(text=f"student will score {y}")
    
    



# frontENd
lbl_1 = Label(text="Enter Study Hours",font=("Arial 20"),bg="magenta",fg="black")
lbl_1.pack(pady=10)

ent_1 = Entry(app,text="",font=("Arial 20"))
ent_1.pack(pady=10)

lbl_2 = Label(text="Enter your Previous Scores",font=("Arial 20"),bg="magenta",fg="black")
lbl_2.pack(pady=10)

ent_2 = Entry(app,text=" ",font=("Arial 20"))
ent_2.pack(pady=10)

lbl_3 = Label(text="Do you ever participated Extracurricular Activities",font=("Arial 20"),bg="magenta",fg="black")
lbl_3.pack(pady=10)

ent_3 = Entry(app,text="   ",font=("Arial 21"))
ent_3.pack(pady=10)

lbl_4 = Label(text="How much time do you Sleep",font=("Arial 20"),bg="magenta",fg="black")
lbl_4.pack(pady=10)

ent_4 = Entry(app,text="    ",font=("Arial 20"))
ent_4.pack(pady=10)

lbl_5 = Label(text="How much you  Practiced Sample Question Papers",font=("Arial 20"),bg="magenta",fg="black")
lbl_5.pack(pady=10)

ent_5 = Entry(app,text="     ",font=("Arial 20"))
ent_5.pack(pady=10)

btn = Button(app,text="Submit",font=("Arial 20"),command=reg)
btn.pack(pady=10)

lbl_shw=  Label(app,font=("Arial 20"),bg="green",fg="black")
lbl_shw.pack(pady=10)



app.mainloop()