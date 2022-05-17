BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

current_card = {}

# load the csv file as a pandas dataframe
df = pd.read_csv("data/french_words.csv")
# turn the data frame into a dictionary
words_dict = df.to_dict(orient="records")

# function to choose a random French word
def show_foreign_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    word = current_card["French"]
    canvas.itemconfig(language_name, text="French", fill="black")
    canvas.itemconfig(foreign_word, text=word, fill="black")
    canvas.itemconfig(canvas_image, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(language_name, text="English", fill="white")
    translation = current_card["English"]
    canvas.itemconfig(foreign_word, text=translation, fill="white")

# create the window
window = Tk()
# add the program title
window.title("Flash Card App")
# set the padding
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# create the canvas for the card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# load the image
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
# place the image on the canvas
canvas_image = canvas.create_image(400, 263, image=front_card_img)
# add words to the card canvas
language_name = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
foreign_word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# create wrong and right buttons
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=show_foreign_word)
right_button = Button(image=right_image, highlightthickness=0, command=show_foreign_word)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

show_foreign_word()

window.mainloop()