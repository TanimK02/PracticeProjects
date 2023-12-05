from tkinter import *

window = Tk()
window.title('M to k convertor')
window.minsize(width=200, height=100)
window.config(pady=15, padx=20)


def calculate():
    km = float(m_entry.get()) * 1.60934
    km = round(km,2)
    k_entry.config(text=km)

miles_txt = Label(text = 'Miles')
miles_txt.grid(column = 2, row = 1)
km_txt = Label(text = 'Km')
km_txt.grid(column = 2, row = 2)
is_equal = Label(text = 'is equal to')
is_equal.grid(column = 0, row = 2)
km = 0
m_entry = Entry(width=8)
m_entry.grid(column=1, row = 1)
k_entry = Label(text=km)
k_entry.grid(column=1, row = 2)

calc_button = Button(text = 'Calculate',command=calculate)
calc_button.grid(column = 1, row = 3)










window.mainloop()