import numpy as np
import tkinter as tk
# from tkinter.ttk import *
import joblib
import pandas as pd

app = tk.Tk()
app.config(bg="#07204a")
app.geometry("560x400")

app.title("Program to check Student perfomance")
model = joblib.load("Student_Performace_classification_Frontend.joblib")

# def check_grades():
def check():
    lst = ["Age","Gender","Ethnicity","ParentalEducation","Absences","Tutoring","ParentalSupport","Extracurricular","Sports","Music","Volunteering","GPA"]
    ent = [ent1, ent2, ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10,ent11,ent12]
    abcs=[]


    for i in ent:
        abc = i.get() 
        abcs.append(abc)


    data_dict = {col: [val] for col, val in zip(lst, abcs)}

    # Create the DataFrame
    df = pd.DataFrame(data_dict)

    grade_pred = model.predict(df)

    output_show.config(text=f"Grade as per the input is {grade_pred}")

lbl1 = tk.Label(text="Age", )
lbl1.grid(row=0, column=1, pady=8)

ent1 = tk.Entry(text = "")  # placeholder="Type your message..."
ent1.grid(row=0, column=2, padx= 19, pady=8)

lbl2 = tk.Label(text="Gender ", )
lbl2.grid(row=0, column=3,padx=2, pady=8)

ent2 = tk.Entry(text = "")
ent2.grid(row=0, column=4, padx=19, pady=8)

lbl3 = tk.Label(text="Ethnicity", )
lbl3.grid(row=1, column=1, pady=8)

ent3 = tk.Entry(text = "")
ent3.grid(row=1, column=2, padx= 19, pady=8)

lbl4 = tk.Label(text="Parental Education", )
lbl4.grid(row=1, column=3,padx=2, pady=8)

ent4 = tk.Entry(text = "")
ent4.grid(row=1, column=4, padx=19, pady=8)


lbl5 = tk.Label(text="Absences", )
lbl5.grid(row=2, column=1, pady=8)

ent5 = tk.Entry(text = "")
ent5.grid(row=2, column=2, padx= 19, pady=8)

lbl6 = tk.Label(text="Tutoring", )
lbl6.grid(row=2, column=3,padx=2, pady=8)

ent6 = tk.Entry(text = "")
ent6.grid(row=2, column=4, padx=19, pady=8)

lbl7 = tk.Label(text="Parental Support", )
lbl7.grid(row=3, column=1, pady=8)

ent7 = tk.Entry(text = "")
ent7.grid(row=3, column=2, padx= 19, pady=8)

lbl8 = tk.Label(text="Extracurricular", )
lbl8.grid(row=3, column=3,padx=2, pady=8)

ent8 = tk.Entry(text = "")
ent8.grid(row=3, column=4, padx=19, pady=8)

lbl9= tk.Label(text="Sports", )
lbl9.grid(row=4, column=1, pady=8)

ent9 = tk.Entry(text = "")
ent9.grid(row=4, column=2, padx= 19, pady=8)

lbl10 = tk.Label(text="Music", )
lbl10.grid(row=4, column=3,padx=2, pady=8)

ent10 = tk.Entry(text = "")
ent10.grid(row=4, column=4, padx=19, pady=8)

lbl11 = tk.Label(text="Volunteering", )
lbl11.grid(row=5, column=1,padx=2, pady=8)

ent11 = tk.Entry(text = "")
ent11.grid(row=5, column=2, padx=19, pady=8)

lbl12 = tk.Label(text="GPA", )
lbl12.grid(row=5, column=3,padx=2, pady=8)

ent12 = tk.Entry(text = "")
ent12.grid(row=5, column=4, padx=19, pady=8)

btn= tk.Button(text= "Check Grades",command=check)
btn.grid(row=6, column=2)

# output = tk.Label (text ="Total Grades" )
# output.grid(row= 7, column= 2,pady=9)

output_show = tk.Label (text = "")
output_show.grid(row=6, column=3)
# img = PotoImage(file = "C:\Users\Farogh\Downloads\Emply.jpeg")  # Img format must be in ong format
# img1 = img.subsample(2,2)



check_grades = {
    "Age": ent1,
    "Gender": ent2,
    "Ethnicity": ent3,
    "Parental Education": ent4,
    "Absences": ent5,
    "Tutoring": ent6,
    "Parental Support": ent7,
    "Extracurricular": ent8,
    "Sports": ent9,	
    "Music": ent10,
    "Volunteering": ent11,
	"GPA": ent12
    
}




app.mainloop()


