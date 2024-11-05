from tkinter.ttk import Combobox

import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("exchange rate",f"exchange {exchange_rate:.2f} for 1 USD")
            else:
                mb.showerror("Error", f"currency {code} not found")
        except Exception as e:
            mb.showerror("Error", f"Error: {e}")
    else:
        mb.showwarning("Warning", "Enter currency code")

window = Tk()
window.title("exchange rate")
window.geometry("360x180")

Label(text="choose currency code").pack(padx=10, pady=10)
cur = ["RUB","EUR", "GBP", "JPY", "CNY", "KZT", "UZS", "CHF", "AED", "CAD"]
combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="get exchange", command=exchange).pack(padx=10, pady=10)

window.mainloop()