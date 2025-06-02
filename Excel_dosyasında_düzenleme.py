import os
os.system("pip install pandas openpyxl")

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Kayıt Yönetim Uygulaması")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        # Başlık
        self.title_label = tk.Label(root, text="Öğrenci Kayıt Yönetimi", font=("Arial", 16), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Excel Yükleme Butonu
        self.load_button = tk.Button(root, text="Excel Dosyası Yükle", command=self.load_file, bg="#4CAF50", fg="white")
        self.load_button.pack(pady=10, padx=20, fill='x')

        # Verileri İşleme Butonu
        self.process_button = tk.Button(root, text="Verileri İşle", command=self.process_data, bg="#2196F3", fg="white")
        self.process_button.pack(pady=10, padx=20, fill='x')

        # Başlık Seçimi
        self.header_label = tk.Label(root, text="Seçilecek Başlıklar:", bg="#f0f0f0")
        self.header_label.pack(pady=10)

        self.header_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.header_listbox.pack(pady=10, padx=20, fill='both', expand=True)

        # Anahtar Başlık Seçimi
        self.key_label = tk.Label(root, text="Anahtar Başlık Seçin (TC Kimlik No / Öğrenci No):", bg="#f0f0f0")
        self.key_label.pack(pady=10)

        self.key_entry = tk.Entry(root)
        self.key_entry.pack(pady=10, padx=20, fill='x')

        # Tekrar Eden Verileri Silme Seçeneği
        self.remove_duplicates_var = tk.BooleanVar()
        self.remove_duplicates_checkbox = tk.Checkbutton(root, text="Tekrar eden verileri sil", variable=self.remove_duplicates_var, bg="#f0f0f0")
        self.remove_duplicates_checkbox.pack(pady=10)

        # Çıktı Alanı
        self.output_text = tk.Text(root, height=5, bg="#ffffff", font=("Arial", 10))
        self.output_text.pack(pady=10, padx=20, fill='both')

        self.data = None

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.data = pd.read_excel(file_path)
            self.output_text.insert(tk.END, f"Dosya Yüklendi: {file_path}\n")
            self.populate_headers()

    def populate_headers(self):
        self.header_listbox.delete(0, tk.END)  # Listeyi temizle
        for column in self.data.columns:
            self.header_listbox.insert(tk.END, column)  # Başlıkları listeye ekle

    def process_data(self):
        if self.data is None:
            messagebox.showwarning("Uyarı", "Önce bir Excel dosyası yükleyin.")
            return

        selected_indices = self.header_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Uyarı", "Lütfen en az bir başlık seçin.")
            return

        selected_headers = [self.header_listbox.get(i) for i in selected_indices]
        key_header = self.key_entry.get().strip()

        if key_header not in self.data.columns:
            messagebox.showwarning("Uyarı", "Anahtar başlık, Excel dosyasında bulunmuyor.")
            return

        # Tekrar eden verileri sil
        if self.remove_duplicates_var.get():
            self.data = self.data.drop_duplicates(subset=[key_header])
            messagebox.showinfo("Bilgi", "Tekrar eden veriler silindi.")

        processed_data = self.data[selected_headers]

        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx;*.xls")])
        if output_path:
            processed_data.to_excel(output_path, index=False)
            messagebox.showinfo("Başarılı", f"Veriler kaydedildi: {output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
