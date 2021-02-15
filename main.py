# Window
# Background color

from tkinter import *
import pandas
import random

# ------------------------------CONSTANTS------------------------------
BACKGROUND_COLOR = "#B1DDC6"
# ------------------------------GLOBALS------------------------------
current_card = {}
# ------------------------------FUNCTIONS------------------------------
def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card =  random.choice(data)
    print(current_card["French"])
    canvas.itemconfig(card_title,text = "French",fill="black")
    canvas.itemconfig(card_word,text = current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text = "English",fill="white")
    canvas.itemconfig(card_word,text = current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)


def is_known():
    data.remove(current_card)
    file_data = pandas.DataFrame(data)
    file_data.to_csv("data/words_to_learn.csv" , index=False) # index= False means don't append the index of the row to the file
    next_card()

# ------------------------------LOAD FILE------------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient = "records")
    print(data)
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient = "records")
# print(data.keys())
# print(data.values())
#print(data.items())

# ------------------------------WINDOW------------------------------
window = Tk()
window.title("Flashy")
window.config(padx = 50,pady = 50,bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)
canvas = Canvas(width = 800 , height = 526)

card_front_image = PhotoImage(file = 'images/card_front.png')
card_back_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400,263,image=card_front_image)
card_title =  canvas.create_text(400,150,text = "Title",font = ("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word", font=("Ariel", 60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row=0,column=0,columnspan=2)

# ------------------------------BUTTONS------------------------------
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image = cross_image, highlightthickness = 0, command = next_card)
unknown_button.grid(column = 0 , row = 1)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image = check_image, highlightthickness = 0, command = is_known)
known_button.grid(column = 1, row = 1)

next_card()

window.mainloop()

