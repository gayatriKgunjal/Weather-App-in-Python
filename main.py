from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry('800x500')

root.resizable(1,1)
f1=Frame()
f1.place(x=0,y=0,width=800,height=500)
f1.configure(background="#E0B0FF")

def weather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
        """{"coord":{"lon":73.9833,"lat":18.5806},"weather":[{"id":803,"main":"Clouds","description":"broken clouds",
        "icon":"04d"}],"base":"stations","main":{"temp":295.55,"feels_like":295.39,"temp_min":295.55,
        "temp_max":295.55,"pressure":1017,"humidity":59,"sea_level":1017,"gr
        nd_level":951},
        "visibility":10000,"wind":{"speed":2.25,"deg":110,"gust":3.34},"clouds":{"all":59},"dt":1668482633,
        "sys":{"country":"IN","sunrise":1668474642,"sunset":1668515203},"timezone":19800,"id":1259652,
        "name":"Wagholi","cod":200}"""
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,',','FEELS','LIKE',temp,'°'))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror('Weather App','Invalid Entry')




#search box
Search_image=PhotoImage(file="tab.png")
myImage=Label(image=Search_image)
myImage.place(x=20,y=20)

textfield=tk.Entry(root,justify='center',width=12,font=('popins',25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=56,y=30)
textfield.focus()

search_icon=PhotoImage(file="search-icon3.png")
myImage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=weather)
myImage_icon.place(x=300,y=33)

#logo
Logo=PhotoImage(file="weather.png")
logo=Label(image=Logo,bg="#404040")
logo.place(x=150, y=170)

#bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=120,pady=25,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND", font=("Helvetica",10,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=190,y=422)

label2=Label(root,text="HUMIDITY", font=("Helvetica",10,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=275,y=422)

label3=Label(root,text="DESCRIPTION", font=("Helvetica",10,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=385,y=422)

label4=Label(root,text="PRESSURE", font=("Helvetica",10,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=525,y=422)

t=Label(font=("arial",30,"bold"),fg="#ee666d")
t.place(x=500,y=250)
c=Label(font=("arial",15,"bold"))
c.place(x=500,y=300)

w=Label(text="...",font=("arial",10,"bold"),bg="#1ab5ef")
w.place(x=190,y=450)

h=Label(text="...",font=("arial",10,"bold"),bg="#1ab5ef")
h.place(x=275,y=450)

d=Label(text="...",font=("arial",10,"bold"),bg="#1ab5ef")
d.place(x=385,y=450)

p=Label(text="...",font=("arial",10,"bold"),bg="#1ab5ef")
p.place(x=525,y=450)

root.mainloop()