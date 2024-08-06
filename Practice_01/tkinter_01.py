import tkinter as tk
from tkinter import *
import joblib

# model1 = joblib.load("Age_Income_Exp_Pred.joblib")

def check_income():
    age = float (name_ent.get())
    exp =float (name_ent1.get())
    op = 31236.21365659112 +(-99.71251284 * age ) + (2183.70891585 + exp)
    res = str(op)
    lblshow.config (text= f"Predicted Income {res[:9]}")

    name_ent.delete (0 , tk.END)  # To clear the entry field.
    name_ent1.delete (0 , tk.END)


app = tk.Tk()
app.geometry("700x400")
app.config (bg="#292929")
app.title("Package Predictor")



lbl = tk.Label(app, text= "Package Predictor", font= ("arial", 16, "bold"))
lbl.pack()
# frame_photo = PhotoImage(file="muhammad-ali-boxer-3840x2160-11119.png")
# frame_label = Label(app,
#                     border=0,
#                     bg='grey',
#                     image=frame_photo,
#                     )

# frame_label.pack()
from PIL import Image, ImageTk

# Open the image file
img = Image.open("muhammad-ali-boxer-3840x2160-11119.png")

# Resize the image without the ANTIALIAS filter
img_resized = img.resize((450, 100))

# Convert the image to PhotoImage
frame_photo = ImageTk.PhotoImage(img_resized)

frame_label = tk.Label(app,
                       border=0,
                       bg='grey',
                       image=frame_photo,
                       )

frame_label.pack()


name_frame = tk.Frame(app, width=200, height=100,
                    borderwidth= 1,)
name_frame.place(x = 20, y = 140)


name_lbl = tk.Label(name_frame , text= "Enter your Age ", font= ("Arial", 18))
name_lbl.pack(side=LEFT)

name_ent = tk.Entry(name_frame, text = "", font= ("Arial", 18),justify= CENTER)
name_ent.pack(side=LEFT)


name_frame1 = tk.Frame(app, width=200, height=100,
                    borderwidth= 1,)
name_frame1.place(x = 20, y = 180)

name_lbl1 = tk.Label(name_frame1 , text= "Enter Experience", font= ("Arial", 18))
name_lbl1.pack(side=LEFT)

name_ent1 = tk.Entry(name_frame1, text = "", font= ("Arial", 18), justify= CENTER)
name_ent1.pack(side=LEFT)



btn = tk.Button (app, text= "Check",font= ("Arial",17),cursor="watch", command=check_income)  #hand2 / toptee
btn.pack(padx=40, pady=96)

lblshow = tk.Label(app, text="", font=("Arial", 18))
lblshow.pack()



app.mainloop()