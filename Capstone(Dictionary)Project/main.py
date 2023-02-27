from tkinter import *
import pandas
import random
BACKGROUND_COLOR="#B1DDC6"
current_card={}
to_learn={}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])



def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    Data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window= Tk()
window.title("Flash-card Game")
window.config(padx=50,pady=50,bg="#B1DDC6")

window.after(3088,func=flip_card)

canvas=Canvas(height=526,width=800)
card_front_img=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg="#B1DDC6",highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


cross_img=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_img,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_img=PhotoImage(file="images/right.png")
known_button=Button(image=check_img,highlightthickness=0)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()
