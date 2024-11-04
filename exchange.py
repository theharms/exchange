from importlib.metadata import entry_points

import requests
import json
from tkinter import *
from tkinter import messagebox as mb



window = Tk()
window.title("exchange rate")
window.geometry("360x180")

Label(text="Enter currency code").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="get exchange", command=exchange).pack(padx=10, pady=10)

window.mainloop()