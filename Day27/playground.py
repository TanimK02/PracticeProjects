from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

my_label['text'] = "new text"
my_label.config(text="New Text")
my_label.config(padx=50,pady=50)

my_label.grid(column = 0, row = 0)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text = "Click Me", command=button_clicked)
button.grid(row=1,column=1)
input = Entry(width=10)
input.grid(row=3, column=3)
print(input.get())




window.mainloop()