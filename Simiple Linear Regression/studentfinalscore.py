import tkinter as tk
import joblib
import numpy as np

model1 = joblib.load("finalscore_prediction.joblib")

def check_score():
    hours = float(ent.get())
    attendence = float(ent2.get())
    y2 = 2.854532842646961 + (3.01355718*hours) + (0.466987*attendence)
    y3 = str(y2)[0 : 5]
    lblhow.config(text = f"Based On Hours studied per day i.e {hours} and Attendance Percentage i.e {attendence}, Your Predicted Final Score is : {y3}")
    
app = tk.Tk()
app.geometry("700x300")
app.title("Predict Student Score")
app.config(bg = "light green")

lbl = tk.Label(app, text = "Enter Hours Studied", font = ("robort", 27, "bold"), background="light green", foreground = "dark green")
lbl.pack(pady = 16)

ent = tk.Entry(app, font = ("robort", 22))
ent.pack()

lbl2 = tk.Label(app, text = "Enter Attendance Percent", font = ("robort", 27, "bold"), background="light green", foreground = "dark green")
lbl2.pack(pady = 16)

ent2 = tk.Entry(app, font = ("robort", 22))
ent2.pack()

btn = tk.Button(app, text = "Check Final Score", font = ("robort", 20, "bold"), fg = "light green", bg = "dark green", command = check_score)
btn.pack(pady = 16)

lblhow = tk.Label(app, text = "", fg = "dark green", bg = "light green", font = ("robort", 16))
lblhow.pack()

lblhow2 = tk.Label(app, text = "", fg = "dark green", bg = "light green", font = ("robort", 16))
lblhow2.pack()

app.mainloop()