import numpy as np
import joblib 
import tkinter as tk

mymodel = joblib.load("SLR_pred.joblib")

app = tk.Tk()

app.geometry ("600x400")
app.config (bg= "#242925")         #fg = "#11d9b4"
app.title ("Student Package Predictor")

def check_pred():
    cgpa = float(inp.get())
    # y= mx+b 
    y = (0.58243437*(cgpa) + (-1.058033562127049))
    y1 = str(y)[0:4]
    lblshow.config (text= f"The predicted package as per the CGPA is {y}")




lbl = tk.Label (app, text = "Student CGPA", font= ("Arial", 18), bg= "#242925", fg = "#11d9b4")
lbl.pack(pady=10)

inp = tk.Entry (app, font= ("Arial", 13))
inp.pack(pady=10)

btn = tk.Button (app, text= "Predict Package", font= ("Arial", 13), bg = "#242925" ,
                 fg = "#11d9b4", command= check_pred)
btn.pack(pady=10)

lblshow = tk.Label (app, text="", font= ("Arial, 13"), bg= "#242925", fg= "#11d9b4")
lblshow.pack()

app.mainloop()