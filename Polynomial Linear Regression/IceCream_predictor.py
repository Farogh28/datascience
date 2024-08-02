import numpy as np 
import joblib
import tkinter as tk
from sklearn.preprocessing import PolynomialFeatures

mymodel = joblib.load("icecream_selling_unit_predictor.joblib")

app = tk.Tk()

app.geometry ("700x400")
app.config (background= "lightgreen")
app.title ("It's Predictor")

def Check_sales():
    tem = inp.get()
    tem = np.array(float(tem))
    # tem = float(inp.get())
    
    tem = tem.reshape (-1,1)
    poly = PolynomialFeatures (degree=2)
    data = poly.fit_transform(tem)

    # print (data[0], 'xxxxxxxxx')
    all_betas = mymodel.coef_
    my_intercept = mymodel.intercept_ 
    print (all_betas)
 
    y= my_intercept + ((all_betas[0] * data[0][0])+ (all_betas[1] * data[0][1] + (all_betas [2]*data[0][2])))
    y= str(y)
    lblshow.config(text=f"Ice Cream Sales Units : {y[:5]}")

    inp.delete (0, tk.END)  # To empty the input field


lbl = tk.Label (app, text=  "Enter the Temprature", 
                font= ("Arial", 30 , "bold"), 
                foreground= "green" , bg= "lightgreen")
lbl.pack( pady= 20)

inp = tk.Entry (font= ("Arial",25), fg= "green")
inp.pack()

btn = tk.Button(app, text= "Check Sales",
                font= ("Arial", 16), bg= "green",fg= "lightgreen", command= Check_sales)
btn.pack(pady=20)

lblshow = tk.Label (app, text= "")
lblshow.pack()



app.mainloop()