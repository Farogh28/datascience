import numpy as np
import joblib
import tkinter as tk
from sklearn.preprocessing import PolynomialFeatures


mymodel = joblib.load ("HeightVsWeight_Predictor.joblib")

app = tk.Tk ()
app.geometry ("700x400")
app.config (bg = "grey")
app.title("Height and weight prediction")

def check_height():
    tem = inp.get ()
    tem = np.array (float (tem))
    tem = tem.reshape (-1,1)
    poly = PolynomialFeatures (degree= 2)
    data = poly.fit_transform(tem)


    betas = mymodel.coef_
    # print (betas)
    my_intercept = mymodel.intercept_


    y= my_intercept + ((betas[0] * data[0][0])+ (betas[1] * data[0][1] + (betas [2]*data[0][2])))
    y = str(y)
    lblshow.config (text = f"Predicted height is (in cm): {y[:6]}")

    inp.delete (0,tk.END)


lbl = tk.Label (app, text= "Enter Age", font= ("Robort",25, "bold"), foreground= "blue" , bg = "black")
lbl.pack(pady=20)


inp = tk.Entry (app, font= ("robort", 16), fg= "skyblue")
inp.pack()

btn = tk.Button (app, text= "Predicted Height in CM is" , font= ("Robort", 20), fg= "orange", bg = "black", command= check_height)
btn.pack(pady= 20)

lblshow = tk.Label (app , font=("Robort", 20), fg = "skyblue", bg = "black")
lblshow.pack()



app.mainloop()