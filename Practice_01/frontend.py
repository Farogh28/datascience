import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

import mysql.connector

import joblib
model = "packge-predictor.joblib"


conn = mysql.connector.connect(host = "localhost", username = "root", password = "@pooja9592", database = "perforace")

curser = conn.cursor()

app = tk.Tk()
app.geometry("940x550")
app.title("Packcgpa Predictor Window")
app.resizable(width=False, height=False)
app.config(bg= "Black")

def chekc_packcgpa():
    name = (name_ent.get())
    cgpa = float(cgpa_ent.get())
    # experience =float(exp_ent.get())
    # y = mx + b
    y = 0.57467027 * cgpa + (-1.0076134311677745)
    output = str(y)
    curser.execute(f"insert into Students values({name}, '{cgpa}', {output[:6]})")
    conn.commit()
    lbl_show.config (text= f"Hey {name}, your predicted packcgpa is {output[:5]} ")

label = tk.Label(app, text= "Packcgpa Predictor", font = ("Arial", 34, "bold"),fg = "#13d1a2", bg = "black")
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

name = tk.Label(app, text="Enter your Name" , font = ("Arial", 18), bg= "black", fg = "#12bec4")
name.place(x=230, y= 185)

name_ent = tk.Entry (app, text = "", font= ("Arial", 18), bg="black", fg = "#12bec4")
name_ent.place(x=480, y=185)

cgpa = tk.Label(app, text="Enter your cgpa" , font = ("Arial", 18), bg= "black", fg = "#12bec4")
cgpa.place(x=230, y= 225)

cgpa_ent = tk.Entry (app, text = "", font= ("Arial", 18), bg="black", fg = "#12bec4")
cgpa_ent.place(x=480, y=225)


# experience = tk.Label(app, text="Enter your Experience" , font = ("Arial", 18), bg= "black", fg = "#12bec4")
# experience.place(x=230, y= 265)

# exp_ent = tk.Entry (app, text = "", font= ("Arial", 18), bg="black", fg = "#12bec4")
# exp_ent.place(x=480, y=265)


btn = tk.Button(app, text= "Check Packcgpa",font= ("Arial", 18), bg="black", fg = "#12bec4", 
                highlightbackground="black", highlightthickness=2,cursor="hand2", command=chekc_packcgpa)
btn.place (x = 390,y= 300)

lbl_show = tk.Label(app, text="", font= ("Arial", 18), bg="black", fg = "#12bec4")
lbl_show.place(x = 250, y = 340)



app.mainloop()