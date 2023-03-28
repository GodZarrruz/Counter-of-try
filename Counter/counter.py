import tkinter as tk
from tkinter import ttk

count = 0

def clicked(): # without event because I use `command=` instead of `bind`
    global count

    count = count + 1

    label1.configure(text=f'Try {count} !')


windows = tk.Tk()
windows.title("Counter test")
windows.geometry("150x60+100+50")
windows.configure(bg="#f2f3f5")
windows.resizable(False,False)
        
label = tk.Label(windows, text="Try",)
label.grid(column=0, row=0)


label1 = tk.Label(windows)
label1.grid(column=0, row=1)

custom_button = ttk.Button(windows, text="+1", command=clicked)
custom_button.grid(column=1, row=0)

windows.mainloop()