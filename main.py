# imports and global valuable
import tkinter as tk


# tk uix
## window
window = tk.Tk()
window.title("Python Calculator")


## entry
display = tk.Entry(window, borderwidth=5, relief="sunken")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=15)


## buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('c', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]
for text, row, col in buttons:
    btn = tk.Button(window, text=text, width=10, height=2, command=lambda x=text: button_click(x))
    btn.grid(row=row, column=col)


def button_click(value):
    if display.get() == "ERROR":
        button_clear()

    if value == "c":
        button_clear()
    elif value == "=":
        button_equal()
    else:
        display.insert(tk.END, value)

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        equation = display.get()
        equation = eval(equation)
        button_clear()
        display.insert(0, equation)
    except:
        button_clear()
        display.insert(0, "ERROR")

# run the program
window.mainloop()