import os
os.system("pip install tk")
os.system("pip install folium")
os.system("pip install tkcalendar")

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import folium

def show_weather():
    city = city_combobox.get()
    district = district_combobox.get()
    selected_date = date_entry.get()

    # Hava durumu simülasyonu
    weather_conditions = {
        "İstanbul": "Güneşli",
        "Ankara": "Parçalı Bulutlu",
        "İzmir": "Yağmurlu"
    }

    weather = weather_conditions.get(city, "Bilinmiyor")
    weather_label.config(text=f"Hava Durumu: {weather}")

    # Harita oluşturma
    if city == "İstanbul":
        map_location = folium.Map(location=[41.0082, 28.9784], zoom_start=10)
    elif city == "Ankara":
        map_location = folium.Map(location=[39.9334, 32.8597], zoom_start=10)
    elif city == "İzmir":
        map_location = folium.Map(location=[38.4192, 27.1287], zoom_start=10)
    else:
        return

    map_location.save('map.html')
    messagebox.showinfo("Map Created", "Harita oluşturuldu: map.html")

# Ana pencere
root = tk.Tk()
root.title("Hava Durumu Uygulaması")
root.geometry("400x400")  # Pencere boyutu

# Tarih girişi
date_label = tk.Label(root, text="Tarih Girin (YYYY-MM-DD):")
date_label.pack(pady=5)
date_entry = tk.Entry(root)
date_entry.pack(pady=5)

# İl ve İlçe seçimi
city_label = tk.Label(root, text="Şehir Seçin:")
city_label.pack(pady=5)
city_combobox = ttk.Combobox(root, values=["İstanbul", "Ankara", "İzmir"])
city_combobox.pack(pady=5)

district_label = tk.Label(root, text="İlçe Seçin:")
district_label.pack(pady=5)
district_combobox = ttk.Combobox(root, values=["Kadıköy", "Çankaya", "Konak"])
district_combobox.pack(pady=5)

# Hava durumu gösterimi
weather_label = tk.Label(root, text="Hava Durumu: ")
weather_label.pack(pady=10)

# Buton
check_weather_button = tk.Button(root, text="Hava Durumunu Kontrol Et", command=show_weather)
check_weather_button.pack(pady=10)

# Ana döngü
root.mainloop()
