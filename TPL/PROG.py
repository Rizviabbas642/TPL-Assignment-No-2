import tkinter as tk
import requests

class CurrencyConverter:
    def _init_(self, master):
        self.master = master
        master.title("Currency Converter")

        # Create input boxes
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1)

        self.from_label = tk.Label(master, text="From:")
        self.from_label.grid(row=1, column=0)

        self.from_var = tk.StringVar(master)
        self.from_var.set("USD")
        self.from_menu = tk.OptionMenu(master, self.from_var, "USD", "EUR", "GBP", "INR", "JPY", "PKR", "AED", "SAR")
        self.from_menu.grid(row=1, column=1)

        self.to_label = tk.Label(master, text="To:")
        self.to_label.grid(row=2, column=0)

        self.to_var = tk.StringVar(master)
        self.to_var.set("EUR")
        self.to_menu = tk.OptionMenu(master, self.to_var, "USD", "EUR", "GBP", "INR", "JPY", "PKR", "AED", "SAR")
        self.to_menu.grid(row=2, column=1)

        # Create conversion button
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=1)

        # Create result label
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def convert(self):
        amount = self.amount_entry.get()
        from_currency = self.from_var.get()
        to_currency = self.to_var.get()

        # Make API request
        url = f"https://v6.exchangerate-api.com/v6/84253d4e421fc4f55749c323/latest/USD/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        # checking API response
        print(response)

        # Parse response
        if response.status_code == 200:
            data = response.json()
            converted_amount = data["conversion_result"]
            self.result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            self.result_label.config(text="Error")

root = tk.Tk()
app = CurrencyConverter(root)
root.mainloop()