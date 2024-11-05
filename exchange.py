from tkinter.ttk import Combobox

import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            response.raise_for_status()
            data = response.json()
            if t_code in data["rates"]:
                exchange_rate = data["rates"][t_code]
                mb.showinfo("exchange rate",f"exchange {exchange_rate:.2f} {t_code} for 1 {b_code}]")

            else:
                mb.showerror("Error", f"currency {t_code} not found")
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
window.geometry("360x350")

Label(text="base currency").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)


Label(text="target currency").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)



t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="get exchange", command=exchange).pack(padx=10, pady=10)

window.mainloop()