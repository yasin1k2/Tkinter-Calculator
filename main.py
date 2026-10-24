# imports and global valuable
import tkinter as tk


# tk uix
## window
window = tk.Tk()
window.title("Python Calculator")


## entry
display = tk.Entry(window, borderwidth=5, relief="sunken")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=15)







# run the program
window.mainloop()