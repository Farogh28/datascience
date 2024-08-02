import numpy as np
import joblib
import tkinter as tk
from sklearn.preprocessing import PolynomialFeatures

model1 = joblib.load("Age_Income_Exp_Pred.joblib")

def check_income():
    age = float (ent.get())
    exp =float (ent2.get())
    op = 31236.21365659112 +(-99.71251284 * age ) + (2183.70891585 + exp)
    res = str(op)
    lblshow.config (text= f"Predicted Income {res[:9]}")

    ent.delete (0 , tk.END)  # To clear the entry field.
    ent2.delete (0 , tk.END)


app = tk.Tk()
app.geometry ("700x400")
app.config (bg="#292929")
app.title ("Income Predictor Tool")

lbl = tk.Label (app, text = "Enter your Age", font= ("Lucida Console", 20), fg ="#CD9B1D" ,bg="#292929" )
lbl.pack(pady=20)

ent = tk.Entry (app, font= ("Lucida Console", 16) )
ent.pack(pady=20)

lbl2 = tk.Label (app, text= "Enter your Experience", font=("Lucida Console",20), fg= "#CD9B1D" ,bg="#292929" )
lbl2.pack()

ent2 = tk.Entry (app, font= ("Lucida console", 16))
ent2.pack(pady=20)

btn = tk.Button (app, text= "Check Predicted Income", font= ("Lucida Console", 17), fg = "#FFC125" , bg ="#454545", command= check_income )
btn.pack()


lblshow = tk.Label (app, text= '', fg= "#3D3D3D" , bg = "grey",
                    font = ("Lucida Console", 16) )
lblshow.pack()

# lblshow2 = tk.Label (app,  text= '', fg= "#3D3D3D" , bg = "grey",
#                     font = ("Lucida Console", 16) )
# lblshow2.pack()


app.mainloop()