import os
os.system("pip install pandas matpllotlib openpyxl")
os.system("pip install tkinter")

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, filedialog, Text, Scrollbar, RIGHT, Y, END, Frame

class ExcelApp:
    def __init__(self, master):
        self.master = master
        master.title("Excel Grafik Uygulaması")

        self.label = Label(master, text="Excel Dosyasını Yükleyin")
        self.label.pack(pady=10)

        # Butonlar için bir çerçeve oluştur
        button_frame = Frame(master)
        button_frame.pack(pady=10)

        self.load_button = Button(button_frame, text="Dosya Yükle", command=self.load_file)
        self.load_button.grid(row=0, column=0, padx=10)

        self.clear_button = Button(button_frame, text="Temizle", command=self.clear_content)
        self.clear_button.grid(row=0, column=1, padx=10)

        self.plot_button = Button(button_frame, text="Grafik Çiz", command=self.plot_graph)
        self.plot_button.grid(row=0, column=2, padx=10)

        self.save_button = Button(button_frame, text="Grafiği Yazdır", command=self.save_graph)
        self.save_button.grid(row=0, column=3, padx=10)

        self.text_area = Text(master, wrap='word', width=50, height=15)
        self.text_area.pack(pady=10)

        self.scrollbar = Scrollbar(master, command=self.text_area.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.df = None  # Veri çerçevesini saklamak için

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.display_file_content(file_path)

    def display_file_content(self, file_path):
        self.text_area.delete(1.0, END)  # Temizle
        self.df = pd.read_excel(file_path)
        self.text_area.insert(END, f"Yüklenen Dosya: {file_path}\n\n")
        self.text_area.insert(END, str(self.df.head()))  # İlk birkaç satırı göster

    def clear_content(self):
        self.text_area.delete(1.0, END)
        self.df = None  # Veri çerçevesini sıfırla

    def plot_graph(self):
        if self.df is None:
            self.text_area.insert(END, "Lütfen önce bir dosya yükleyin.\n")
            return

        plt.style.use('ggplot')  # ggplot stilini kullan
        plt.figure(figsize=(12, 8))

        # X eksenindeki değerleri metin formatına çevir
        x_labels = self.df.iloc[:, 0].astype(str)

        # Y değerlerini kontrol et ve temizle
        y_values = pd.to_numeric(self.df.iloc[:, 1], errors='coerce').dropna()
        if len(y_values) == 0:
            self.text_area.insert(END, "Geçerli Y değerleri yok.\n")
            return

        # Dikey çubuklar
        plt.barh(x_labels[:len(y_values)], y_values, color=plt.cm.viridis(range(len(y_values))))
        plt.title('Excel Verileri Grafiği', fontsize=22, fontweight='bold')
        plt.xlabel('Y Eksen Başlığı', fontsize=16)
        plt.ylabel('X Eksen Başlığı', fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)

        # Değerleri grafiğin yanında ekleme
        for i, v in enumerate(y_values):
            plt.text(v + 5, i, str(v), color='black', fontsize=10, va='center')

        plt.tight_layout()
        plt.show()

    def save_graph(self):
        if self.df is None:
            self.text_area.insert(END, "Lütfen önce bir dosya yükleyin ve grafik çizin.\n")
            return
        plt.savefig('grafik.png')  # Grafiği dosyaya kaydet
        self.text_area.insert(END, "Grafik 'grafik.png' olarak kaydedildi.\n")

if __name__ == "__main__":
    root = Tk()
    app = ExcelApp(root)
    root.mainloop()
