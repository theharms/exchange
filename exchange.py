from tkinter.ttk import Combobox

import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def update_cur_label(event):
    code = combobox.get()
    name = cur[code]
    cur_label.config(text=name)

def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("exchange rate",f"exchange {exchange_rate:.2f} {code} for 1 USD")

            else:
                mb.showerror("Error", f"currency {code} not found")
        except Exception as e:
            mb.showerror("Error", f"Error: {e}")
    else:
        mb.showwarning("Warning", "Enter currency code")

cur = {
    "RUB":"Российский рубль",
    "EUR":"Евро",
    "GBP":"Британский фунт",
    "JPY":"Японская йена",
    "CNY":"Китайский юань",
    "KZT":"Казайский тенге",
    "UZS":"Узбекский сом",
    "CHF":"",
    "AED":"",
    "CAD":""
       }

window = Tk()
window.title("exchange rate")
window.geometry("360x180")

Label(text="choose currency code").pack(padx=10, pady=10)
combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_cur_label)

cur_label = ttk.Label()
cur_label.pack(padx=10, pady=10)

Button(text="get exchange", command=exchange).pack(padx=10, pady=10)

window.mainloop()