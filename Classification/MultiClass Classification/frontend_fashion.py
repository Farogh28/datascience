import numpy as np
import joblib
import tkinter as tk

from tkinter import filedialog       # To upload image
# PIL -- Pillow
from PIL import Image , ImageTk

items = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",  "Sandal",  "Shirt", "Sneaker", "Bag", "Ankle boot"]


model = joblib.load("fashion-image-predictor.joblib")

# from sklearn.preprocessing import PolynomialFeatures

def image_predictor(image_path):   # Created a funcn with a parameter, 
    img = Image.open(image_path)
    resize_img = img.convert ("L").resize((28,28))  # L -- > Convert image into GreyScale

    img_array = np.array (resize_img)     #resize the image 

    # 1 D me covert krne ke liye we use Flatten function
    convert_to_oneD = img_array.flatten () 

    if convert_to_oneD.shape != (784,):
            predictor_result.config (text= f"The result is ")
    
    else:
         my_image = model.predict(convert_to_oneD.reshape(1,-1))
    return my_image

    #Reshape the data

    

def upload_image ():
    # print ("Hello")
    filepath = filedialog.askopenfilename()
    # print(filepath)
    myimg = Image.open(filepath)
    # resize_image = myimg.thumbnail(("400x400"))
    myimg.thumbnail((400, 400))   #OR
    img = ImageTk.PhotoImage(myimg)
    
    imgshow.config (image= img)   # Same syntax as to modify the text, over here its modigying the image
    imgshow.image = img

    #Calling the above function
    result = image_predictor(filepath)
    predictor_result.config (text= f"The result is {items[result[0]]}")

app = tk.Tk()

app.geometry("700x500")
app.title("Image Classification")
app.config (bg = "#a5f25c")

lbl = tk.Label(app, text= "Fashion Item predictor", font= ("Arial", 24, "bold" ),
               bg= "#a5f25c", fg= "#276312")
lbl.pack(pady=10)


btn = tk.Button (app, text= "Upload Image", font= ("Arial", 16 , "bold") , bg= "#276312", fg= "#a5f25c" , command= upload_image )
btn.pack(pady= 10)

imgshow = tk.Label(app, )
imgshow.pack(pady= 10)

predictor_result = tk.Label (app,  font= ("Arial", 17, "bold" ),bg= "#a5f25c", fg= "#276312")
predictor_result.pack()


app.mainloop()