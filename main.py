import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import requests

window = ctk.CTk()
window.title("Weather In Your Cıty")
window.geometry("420x730")
window.configure(fg_color="#38b6ff")

apiKey = "c7c6fdb3614204ce87205f65580322dd"

#Images
imageCloud = Image.open("weatherBackground/cloudbg.png")
ctk_image_cloud = ctk.CTkImage(light_image=imageCloud, dark_image=imageCloud, size=(200, 200))

imageCl2 = Image.open("weatherBackground/cl2.png")
ctk_image_cl2 = ctk.CTkImage(light_image=imageCl2, dark_image=imageCl2, size=(300, 300))

imageWeather = Image.open("weatherBackground/sun.png")
ctk_image_weather = ctk.CTkImage(light_image=imageWeather, dark_image=imageWeather, size=(200, 200))

imageWeather2 = Image.open("weatherBackground/FOGGY.png")
ctk_image_weather2 = ctk.CTkImage(light_image=imageWeather2, dark_image=imageWeather2, size=(200, 200))

imageWeather3 = Image.open("weatherBackground/rainyNew.png")
ctk_image_weather3 = ctk.CTkImage(light_image=imageWeather3, dark_image=imageWeather3, size=(200, 200))

imageWeather4 = Image.open("weatherBackground/snowfall.png")
ctk_image_weather4 = ctk.CTkImage(light_image=imageWeather4, dark_image=imageWeather4, size=(200, 200))

imageWeather5 = Image.open("weatherBackground/thunder.png")
ctk_image_weather5 = ctk.CTkImage(light_image=imageWeather5, dark_image=imageWeather5, size=(200, 200))

imageWeather6 = Image.open("weatherBackground/cloudlyNew.png")
ctk_image_weather6 = ctk.CTkImage(light_image=imageWeather6, dark_image=imageWeather6, size=(200, 200))

logoImage = Image.open("weatherBackground/logo1.png")
ctk_image_logo = ctk.CTkImage(light_image=logoImage, dark_image=logoImage,size=(200,200))

def showAlert():
    messagebox.showwarning(title="Warning",message="THIS CITY WAS NOT FOUND")

# a function to show weather images and information
def IdName(id):
    if 500 <= id <= 531:
        labelWea.configure(image=ctk_image_weather3)
        return "RAINY"
    if 600 <= id <= 631:
        labelWea.configure(image=ctk_image_weather4)
        return "SNOWY"
    if 701 <= id <= 781:
        labelWea.configure(image=ctk_image_weather2)
        return "FOGGY"
    if id == 800:
        labelWea.configure(image=ctk_image_weather)
        return "CLEAR"
    if 801 <= id <= 804:
        labelWea.configure(image=ctk_image_weather6)
        return "CLOUDLY"
    if 200 <= id <= 232:
        labelWea.configure(image=ctk_image_weather5)
        return "STORMY"
    else:
        raise ValueError("id was not found")

# a function to get weather information
def get_weather():
    city = city_entry.get()
    geo_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={apiKey}"
    responseGeo = requests.get(geo_api)
    lat_lon = responseGeo.json()
    if lat_lon:
        latCity = lat_lon[0]["lat"]
        lonCity = lat_lon[0]["lon"]
        weaApi = f"https://api.openweathermap.org/data/3.0/onecall?lat={latCity}&lon={lonCity}&appid={apiKey}&units=metric"
        responseWea = requests.get(weaApi)
        data_wea = responseWea.json()
        print(latCity, lonCity)

        if data_wea:
            weaId = data_wea["current"]["weather"][0]["id"]
            weaCels = int(data_wea["current"]["temp"])
            weather = IdName(weaId)
            print(weather,weaCels)

            labelCelsius.configure(text=f"{weaCels}°C",font=("Segoe UI", 100))
            labelCelsius.place(x=210, y=340)
            labelCelsius.update()
            celsiusX2 = labelCelsius.winfo_width()
            labelCelsius.place(x=210 - (celsiusX2 / 2), y=340)

            labelCity.configure(text=city.upper())
            labelCity.update()
            cityX2 = labelCity.winfo_width()
            labelCity.place(x=210 - (cityX2 / 2), y=120)

            labelWeaType.configure(text=weather, font=("Segoe UI", 50))
            labelWeaType.place(x=100, y=450)
            labelWeaType.update()
            weaTypeX2 = labelWeaType.winfo_width()
            labelWeaType.place(x=210 - (weaTypeX2 / 2), y=450)

        else:
            showAlert()
    else:
        showAlert()


#labels of clouds
labelCloud = ctk.CTkLabel(master=window,fg_color="transparent",image=ctk_image_cloud,text="",width=200,height=200)
labelCloud.place(x=-100,y=-50)

labelCloud2 = ctk.CTkLabel(master=window,fg_color="transparent",image=ctk_image_cloud,text="",width=200,height=200)
labelCloud2.place(x=330,y=-50)

labelCloud3 = ctk.CTkLabel(master=window,fg_color="transparent",image=ctk_image_cloud,text="",width=200,height=200)
labelCloud3.place(x=270,y=120)

labelCloud3 = ctk.CTkLabel(master=window, fg_color="transparent", image=ctk_image_cl2, text="", width=300, height=300)
labelCloud3.place(x=230,y=260)

labelCloud4 = ctk.CTkLabel(master=window, fg_color="transparent", image=ctk_image_cl2, text="", width=300, height=300)
labelCloud4.place(x=210,y=460)

labelCloud5 = ctk.CTkLabel(master=window, fg_color="transparent", image=ctk_image_cl2, text="", width=300, height=300)
labelCloud5.place(x=-150,y=440)

labelCloud6 = ctk.CTkLabel(master=window,fg_color="transparent",image=ctk_image_cloud,text="",width=200,height=200)
labelCloud6.place(x=-60,y=170)

labelCloud7 = ctk.CTkLabel(master=window,fg_color="transparent",image=ctk_image_cloud,text="",width=200,height=200)
labelCloud7.place(x=60,y=615)

labelCloud8 = ctk.CTkLabel(master=window, fg_color="transparent", image=ctk_image_cl2, text="", width=300, height=300)
labelCloud8.place(x=70,y=-140)




# label of background and title
labelTitle = ctk.CTkLabel(master=window, text="THE WEATHER", font=("Segoe UI", 22,"bold")
                   ,fg_color="#0786d0",text_color="#ffde59",padx= 5,pady = 5,corner_radius=8)
labelTitle.place(x=126,y=60)


labelBg = ctk.CTkLabel(master=window, text="", font=("Segoe UI", 20)
                   ,fg_color="#0786d0",corner_radius=10,padx=155,pady=205)
labelBg.place(x=45,y=110)


#Label weather
labelWea = ctk.CTkLabel(master=window, fg_color="#0786d0", image=ctk_image_logo,text="", width=200,height=200)
labelWea.place(x=115,y=160)

labelCelsius = ctk.CTkLabel(master=window,text="THE WEATHER",text_color="#ffde59", fg_color="#0786d0",
                            font=("Segoe UI", 40))
labelCelsius.place(x= 210-128,y=380)


labelWeaType = ctk.CTkLabel(master=window, text="IN YOUR CITY", text_color="#ffde59", fg_color="#0786d0",
                            font=("Segoe UI", 30))
labelWeaType.place(x=210-92.5,y=430)
labelWeaType.update()
print(labelWeaType.winfo_width())

labelCity = ctk.CTkLabel(master=window, text="", text_color="#ffde59", fg_color="#0786d0",font=("Segoe UI", 30,"bold"))
labelCity.place(x=140,y=120)


#entry
city_entry = ctk.CTkEntry(master=window, placeholder_text="ENTER YOUR CITY",
                          placeholder_text_color="#ffde59",
                          bg_color="#38b6ff",
                          fg_color="#0786d0",
                          justify="center",
                          width=180,
                          height=32,
                          text_color="#ffde59",
                          border_color="#38b6ff",
                          font=("Segoe UI", 15,"bold"),
                          corner_radius=10)
city_entry.place(x=120,y=570)

#button
city_button = ctk.CTkButton(master=window,
                            fg_color="#0786d0",
                            text="GET",
                            text_color="#ffde59",
                            width=80,
                            command=get_weather,
                            font=("Segoe UI", 15,"bold"),
                            corner_radius=10)
city_button.place(x=170,y=610)



window.mainloop()