BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *


# create the window
window = Tk()
# add the program title
window.title("Flash Card App")
# set the padding
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create the canvas for the card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# load the image
front_card_img = PhotoImage(file="images/card_front.png")
# place the image on the canvas
canvas.create_image(400, 263, image=front_card_img)
# add words to the card canvas
language_name = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
foreign_word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# create wrong and right buttons
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
right_button = Button(image=right_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

window.mainloop()