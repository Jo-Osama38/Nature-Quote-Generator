import os
import random
from PIL import Image ,ImageTk
from tkinter import Tk,Label,Button

BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "images")
images = [os.path.join(IMAGES_DIR, f) for f in os.listdir(IMAGES_DIR) 
          if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]

text = [
    "Believe in yourself and all that you are.", 
    "The best is yet to come.", 
    "Your potential is endless.",
    "Difficult roads often lead to beautiful destinations.", 
    "Focus on the good, and the good will get better.", 
    "Don’t stop until you are proud.", 
    "Every day is a second chance.",
    "Happiness is a choice, not a result.",
    "What a breathtaking view!", 
    "Nature is absolutely wonderful." 
]

#function for random chioce
def random_choice():
    if images:
        try:
            #random choice
            image_choice = random.choice(images)
            text_choice = random.choice(text)
            # open image
            image = Image.open(image_choice)
            image = image.resize((400,300))
            image_tk = ImageTk.PhotoImage(image)

            #change of elements
            label_image.config(image=image_tk)
            label_image.image = image_tk
            label_text.config(text=text_choice)
        except Exception:
            label_text.config(text="Cannot opem image 😢")

    else:
        print("Image not found 😢")


# tkinter
page = Tk()
page.title("Nature Quote Viewer 🌿")
page.geometry("400x450+500+150")
page.configure(bg="black")
page.resizable(0,0)

label_image = Label(page,bg="black")
label_image.pack(pady=10)

label_text =Label(page,text="",font=("Arial", 15), fg="green",background="black")
label_text.pack(pady=10)

buttom = Button(page,text="NEXT=>",font=("Arial",15,"bold"),command=random_choice,
                relief="flat",padx=1,pady=1)
buttom.pack(pady=10)

random_choice()

page.mainloop()
