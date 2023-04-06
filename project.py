from tkinter import Tk, ttk
from tkinter import *
from PIL import Image,ImageTk
import requests
import json

window = Tk()

col = "#607be6"

window.geometry("400x480")
window.title("Currency Converter")
window.resizable( height= FALSE, width= TRUE )

top = Frame(window, width= 400, height= 60, bg= col)
top.grid(row= 0, column= 0)

main = Frame (window, width= 400, height= 400)
main.grid(row= 1, column= 0)

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

logo = Image.open("D:/Python Programs/TKINTER/2285848-200.png")
logo = logo.resize((40, 40))
logo = ImageTk.PhotoImage(logo)
app_name = Label( top, image= logo, compound=LEFT, text= "Currency Converter", height= 20, padx= 15, pady= 15, font=("Algerian", 16), bg= col, fg= "#ffffff", anchor=CENTER ) 
app_name.place(x= 30, y= 3)

result = Label(main, height= 2, width= 16, relief= "solid", anchor= CENTER, font= ("Georgia",22), fg= "#000000" )
result.place(x= 60, y= 30)

currency = ['USD','INR','OMR','EUR','BRL','CAD']

From = Label(main, text= "From", height= 2, width= 13, relief= "flat", anchor= NW, font= ("Georgia"), fg= "#000000")
From.place(x= 60,y= 140)
combo1 = ttk.Combobox(main, width = 10, justify = CENTER, font= ("Georgia")) 
combo1["values"] = (currency)
combo1.place(x=60, y=170)

To = Label(main, text= "To", height= 2, width= 13, relief= "flat", anchor= NW, font= ("Georgia"), fg= "#000000")
To.place(x= 210,y= 140)
combo2 = ttk.Combobox(main, width = 10, justify = CENTER, font= ("Georgia")) 
combo2["values"] = (currency)
combo2.place(x=210, y=170)

value = Entry(main, width=13,  justify= CENTER, relief=SOLID,font= ("Georgia",26) )
value.place(x=60,y=215)

convert = Button(main, text = "CONVERT", width= 29, padx= 5, pady= 5, bg=col, fg= "#000000", font= ("Georgia"),command = convert)
convert.place(x=60,y=280)

window.mainloop()