import requests
import json
from tkinter import *
from tkinter import messagebox
def weather():
    try:
        global city
        city=entry_field.get()
        parameters={}
        main_url="http://api.openweathermap.org/data/2.5/weather?"
        parameters['appid']='c0e6390d1a42ff4ef5e6b839801f7b7e'
        parameters['q']=city

        file=requests.get(main_url,params=parameters).json()
        #print(file)
        basic_weather=file['main']
        temperature=int(basic_weather['temp'])-273#the unit was kelvin
        pressure=basic_weather['pressure']#hpa
        humidity=basic_weather['humidity']#//percentage
        print(temperature)
        print(pressure)
        print(humidity)
        label52 = Label(root,bg='#8B92EF').grid(column=1, row=4, pady=15)
        label5 = Label(root, text="Temp: {} degree celcius ".format(temperature),bg='#8B92EF',font="Cambria").grid(column=1, row=5, pady=15)
        label6 = Label(root, text="Pressure: {} hPa ".format(pressure),bg='#8B92EF',font="Cambria").grid(column=1, row=6, pady=15)
        label7 = Label(root, text="Humidity: {}% ".format(humidity),bg='#8B92EF',font="Cambria").grid(column=1, row=7, pady=15)
    except:
        error=messagebox.showerror("Error!!","Please enter a valid city!!")
root=Tk()
root.title('Basic current weather app')
root.configure(bg='#8B92EF')
root.geometry('500x500')
root.iconbitmap('1.ico')
#===================================the title=================#
frame1=Frame(root,bg='white',height=100,width=500).grid(column=0,row=0,columnspan=3)
title_1=Label(frame1,text='Weather App',font=('Cambria',29),bg='white').grid(column=1,row=0)


label1=Label(root,text="Enter the name of your city below: ",bg='#8B92EF' ,font="Cambria").grid(column=1,row=1,pady=15)
entry_field=Entry(root,width=45)
entry_field.grid(column=1,row=2,pady=20)
city = entry_field.get()
button_1=Button(root,text="CONFIRM!!",pady=10,bg='white',command=weather).grid(column=1,row=3)


root.mainloop()

