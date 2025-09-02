from tkinter import Tk, ttk
from tkinter import *
from PIL import Image,ImageTk
import requests
import json

window = Tk()

col = "#607be6"

window.geometry("600x400")  # start with a larger window
window.minsize(400, 300)    # minimum size for responsiveness
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=5)
window.columnconfigure(0, weight=1)

window.title("Currency Converter")

top = Frame(window, bg=col)
top.grid(row=0, column=0, sticky="nsew")
top.grid_columnconfigure(0, weight=1)

main = Frame(window)
main.grid(row=1, column=0, sticky="nsew")
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)


def convert ():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
        "X-RapidAPI-Key": "d317b65ed9msh8bf8eff9997dd96p10c7d8jsn76e166961575",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"    
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amt = data["result"]["convertedAmount"]
    roundoff = "{:,.2f}".format(converted_amt)
    
    result["text"] = roundoff

    print(roundoff)

logo = Image.open("D://Downloads/Currency_Converter-Tkinter-main/Currency_Converter-Tkinter-main/2285848-200.png")
logo = logo.resize((40, 40))
logo = ImageTk.PhotoImage(logo)
app_name = Label( top, image= logo, compound=LEFT, text= "Currency Converter", height= 20, padx= 15, pady= 15, font=("Algerian", 16), bg= col, fg= "#ffffff", anchor=CENTER ) 
app_name.grid(row=0, column=0, sticky="w", padx=20, pady=5)

result = Label(main, height= 2, width= 16, relief= "solid", anchor= CENTER, font= ("Georgia",22), fg= "#000000" )
result.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")


currency = ['USD','INR','OMR','EUR','BRL','CAD']

From = Label(main, text= "From", height= 2, width= 13, relief= "flat", anchor= NW, font= ("Georgia"), fg= "#000000")
From.grid(row=1, column=0, pady=10, sticky="e")
combo1 = ttk.Combobox(main, width = 10, justify = CENTER, font= ("Georgia")) 
combo1["values"] = (currency)
combo1.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

To = Label(main, text= "To", height= 2, width= 13, relief= "flat", anchor= NW, font= ("Georgia"), fg= "#000000")
To.grid(row=1, column=1, pady=10, sticky="w")
combo2 = ttk.Combobox(main, width = 10, justify = CENTER, font= ("Georgia")) 
combo2["values"] = (currency)
combo2.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

value = Entry(main, width=13,  justify= CENTER, relief=SOLID,font= ("Georgia",26) )
value.grid(row=3, column=0, columnspan=2, padx=20, pady=15, sticky="ew")

convert_btn = Button(main, text = "CONVERT", width= 29, padx= 5, pady= 5, bg=col, fg= "#000000", font= ("Georgia"),command = convert)
convert_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

window.mainloop()
