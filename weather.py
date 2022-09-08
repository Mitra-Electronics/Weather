from tkinter import Canvas, Tk, Label, Entry, messagebox
from PIL import Image
from PIL.ImageTk import PhotoImage
from os.path import join
from requests import get
from requests.exceptions import ConnectionError
from time import strftime, gmtime

def get_weather(canvas):
    city = text_field.get()
    try:
        json_data = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=06c921750b9a82d8f5d1294e1586276f&units=metric").json()
        condition = json_data["weather"][0]["main"]
        place = json_data["name"]
        temp = json_data["main"]["temp"]
        feels_like = json_data["main"]["feels_like"]
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        sunrise = strftime("%I:%M:%S", gmtime(json_data["sys"]["sunrise"] + json_data["timezone"]))
        sunset = strftime("%I:%M:%S", gmtime(json_data["sys"]["sunset"] + json_data["timezone"]))

        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = f"\n\nFeels Like: {feels_like} °C\nPressure: {pressure}\nHumidity: {humidity}%\nWind Speed: {wind}km/h\nSunrise: {sunrise}\nSunset: {sunset}"
        imag = Image.open(join("assets", json_data["weather"][0]["icon"]+".png"))
        img = PhotoImage(imag.resize((100, 100)))
        img1.configure(image=img)
        img1.image = img
        place_label.config(text=place)
        condition_label.config(text = final_info)
        label2.config(text = final_data)
    except ConnectionError:
        messagebox.showerror(title="No Internet", message="No Internet Connection. Please make sure that you are connected to the internet in order for the app to work.")


tk = Tk()
tk.geometry("700x600")
tk.title("Weather App")
tk.resizable(False, False)
f = ("poppins", 20, "bold")
t = ("poppins", 32, "bold")

text_field = Entry(tk, justify="center", width = 20, font = t)
text_field.pack(pady = 20, anchor="n")
text_field.focus()
text_field.bind("<Return>", get_weather)

canvas1 = Canvas(tk)
canvas1.pack(anchor="n")
canvas2 = Canvas(tk)
canvas2.pack(anchor="s")

img1 = Label(canvas1)
img1.pack(side="left", anchor="n")
condition_label = Label(canvas1, font=t)
condition_label.pack(side="left", anchor="n")
place_label = Label(canvas1, font=t)
place_label.pack(side="right", anchor="n")
label2 = Label(canvas2, font=f)
label2.pack(side="bottom",anchor="s")
tk.mainloop()