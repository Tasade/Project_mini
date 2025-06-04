import os
os.system("pip install vaderSentiment")
os.system("pip install tkinter")
os.system("pip install requests")

import tkinter as tk
from tkinter import messagebox
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # veya TextBlob

class SocialMediaAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("Sosyal Medya Duygu Durumu Analizi")
        master.configure(bg="#f9f9f9")  # Pastel arka plan rengi

        # API anahtarı
        self.api_key = None

        # Kullanıcı arayüzü bileşenlerini tanımlayın
        self.setup_ui()
        
        # Duygu analizi aracı
        self.analyzer = SentimentIntensityAnalyzer()

    def setup_ui(self):
        # API Anahtarı Girişi
        self.api_key_label = tk.Label(self.master, text="API Anahtarı:", bg="#f9f9f9", font=("Arial", 12))
        self.api_key_label.pack(pady=5)
        self.api_key_entry = tk.Entry(self.master, bg="#e0f7fa", font=("Arial", 12))
        self.api_key_entry.pack(pady=5)

        self.save_button = tk.Button(self.master, text="Kaydet", command=self.save_api_key, bg="#b2ebf2", font=("Arial", 12))
        self.save_button.pack(pady=10)

        # Kullanıcı adı girişi
        self.username_label = tk.Label(self.master, text="Kullanıcı Adı:", bg="#f9f9f9", font=("Arial", 12))
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.master, bg="#e0f7fa", font=("Arial", 12))
        self.username_entry.pack(pady=5)

        self.login_button = tk.Button(self.master, text="Giriş Yap", command=self.login, state='disabled', bg="#b2ebf2", font=("Arial", 12))
        self.login_button.pack(pady=10)

        self.analyze_button = tk.Button(self.master, text="Analiz Et", command=self.analyze, state='disabled', bg="#b2ebf2", font=("Arial", 12))
        self.analyze_button.pack(pady=10)

        self.progress = tk.Scale(self.master, from_=0, to=100, orient='horizontal', length=300, bg="#e0f7fa")
        self.progress.pack(pady=10)

        self.emoji_label = tk.Label(self.master, text="", font=("Arial", 24), bg="#f9f9f9")
        self.emoji_label.pack(pady=10)

    def save_api_key(self):
        self.api_key = self.api_key_entry.get()
        if self.api_key:
            messagebox.showinfo("Başarılı", "API anahtarı kaydedildi!")
            self.login_button['state'] = 'normal'
        else:
            messagebox.showerror("Hata", "Lütfen geçerli bir API anahtarı girin.")

    def login(self):
        username = self.username_entry.get()
        try:
            response = requests.get(f'https://api.socialmedia.com/user/{username}', headers={'Authorization': f'Bearer {self.api_key}'}, timeout=10)
            response.raise_for_status()
            self.user_data = response.json()
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            self.analyze_button['state'] = 'normal'
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

    def analyze(self):
        posts = self.user_data['posts']
        sentiments = [self.analyzer.polarity_scores(post['content'])['compound'] for post in posts]
        average_sentiment = sum(sentiments) / len(sentiments) * 100
        self.progress.set(average_sentiment)
        self.emoji_label.config(text="😊" if average_sentiment >= 0 else "😡")

if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaAnalyzer(root)
    root.mainloop()
