from tkinter import *
from word_manager import WordManager

BACKGROUND_COLOR = "#B1DDC6"
french = "French"
english = "English"

# word manager
word_manager = WordManager()


def change_word():
    canvas.itemconfig(language, text=french)
    canvas.itemconfig(word, text = word_manager.choose_word())
    canvas.itemconfig(flash_side, image = flash_front_img)
    window.after_cancel(window)
    window.after(3000, flip_word)


def change_n_save():
    canvas.itemconfig(language, text=french)
    canvas.itemconfig(word, text = word_manager.choose_word())
    canvas.itemconfig(flash_side, image = flash_front_img)
    window.after_cancel(window)
    window.after(3000, flip_word)
    word_manager.remove_pair()

def flip_word():
    canvas.itemconfig(flash_side, image=flash_back_img)
    canvas.itemconfig(language, text=english)
    canvas.itemconfig(word, text = word_manager.english_word() )

def start():
    window.after_cancel(window)
    window.after(3000, flip_word)


# window
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# flashcards
flash_front_img = PhotoImage(file="images/card_front.png")
flash_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_side = canvas.create_image(400, 265, image=flash_front_img)
language = canvas.create_text(400, 150, text=french, fill='black', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text=word_manager.choose_word(), fill='black', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# wrong button
wrong_img = PhotoImage(file='images/wrong.png')
wrong = Button(image=wrong_img, bd=0, highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=change_word)
wrong.grid(column=0, row=1)

# right button
right_img = PhotoImage(file='images/right.png')
right = Button(image=right_img, bd=0, highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=change_n_save)
right.grid(column=1, row=1)



window.mainloop()
