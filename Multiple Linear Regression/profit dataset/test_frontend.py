import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

import joblib
model = "profit_dataset.joblib"

app = tk.Tk()
app.geometry("940x550")
app.title("Package Predictor Window")
app.resizable(width=False, height=False)
app.config(bg= "Black")

def chekc_package():
    R_D_Spend = (name_ent.get())
    Administration = float(age_ent.get())
    Marketing_Spend =float(exp_ent.get())
    # result = (fourmula)
    # output = str(result)
    lbl_show.config (text= f"Hey {name}, your predicted package is ")

label = tk.Label(app, text= "Package Predictor", font = ("Arial", 34, "bold"),fg = "#13d1a2", bg = "black")
label.place(x= 280, y = 7)

img = Image.open("desktop-wallpaper-do-i-wanna-know-beatbox-cover-beatbox-emre.png")
img_resized = img.resize((940, 118))

frame_photo = ImageTk.PhotoImage(img_resized)

frame_label = tk.Label(app,
                       border=0,
                       bg='grey',
                       image=frame_photo,
                       )

frame_label.place(x = 9, y= 60)

R_D_Spend = tk.Label(app, text="Enter your Name" , font = ("Arial", 18), bg= "black", fg = "#12bec4")
R_D_Spend.place(x=230, y= 185)

name_ent = tk.Entry (app, text = "", font= ("Arial", 18), bg="black", fg = "#12bec4")
name_ent.place(x=480, y=185)

Administration = tk.Label(app, text="Enter your Age" , font = ("Arial", 18), bg= "black", fg = "#12bec4")
Administration.place(x=230, y= 225)

age_ent = tk.Entry (app, text = "", font= ("Arial", 18), bg="black", fg = "#12bec4")
age_ent.place(x=480, y=225)


Marketing_Spend = tk.Label(app, text="Enter your Experience" , font = ("Arial", 18), bg= "black", fg = "#12bec4")
Marketing_Spend.place(x=230, y= 265)

exp_ent = tk.Entry (app, text = "", font= ("Arial", 18), bg="black", fg = "#12bec4")
exp_ent.place(x=480, y=265)


btn = tk.Button(app, text= "Check Package",font= ("Arial", 18), bg="black", fg = "#12bec4", 
                highlightbackground="black", highlightthickness=2,cursor="hand2", command=chekc_package)
btn.place (x = 390,y= 340)

lbl_show = tk.Label(app, text="", font= ("Arial", 18), bg="black", fg = "#12bec4")
lbl_show.place(x = 290, y = 380)



app.mainloop()