import tkinter as tk
from tkinter import ttk

def show_form():
    next_button.grid_forget()  # Menghapus tombol Next setelah ditekan
    label_nama.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_nama.grid(row=1, column=1, padx=5, pady=5)
    label_alamat.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_alamat.grid(row=2, column=1, padx=5, pady=5)
    label_makanan.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    combo_makanan.grid(row=3, column=1, padx=5, pady=5)
    submit_button.grid(row=4, columnspan=2, padx=5, pady=5)

# Membuat instance Tkinter
root = tk.Tk()
root.title("Program Kecerdasan Buatan")

# Label selamat datang
label_welcome = ttk.Label(root, text="SELAMAT DATANG DI PROGRAM REKOMENDASI LAPTOP", font=("Helvetica", 14, "bold"))
label_welcome.grid(row=0, columnspan=2, padx=10, pady=10)

# Tombol Next
next_button = ttk.Button(root, text="Next", command=show_form)
next_button.grid(row=1, columnspan=2, padx=5, pady=5)

# Membuat label dan input field untuk nama
label_nama = ttk.Label(root, text="Nama:")
entry_nama = ttk.Entry(root)

# Membuat label dan input field untuk alamat
label_alamat = ttk.Label(root, text="Alamat:")
entry_alamat = tk.Text(root, width=30, height=5)

# Membuat label dan selectbox untuk makanan favorit
label_makanan = ttk.Label(root, text="Makanan Favorit:")
makanan_list = ["Nasi Goreng", "Mie Ayam", "Sate", "Gado-gado"]
combo_makanan = ttk.Combobox(root, values=makanan_list)

# Tombol Submit
def submit():
    nama = entry_nama.get()
    alamat = entry_alamat.get("1.0", "end-1c")  # Mendapatkan teks dari input alamat
    makanan_favorit = combo_makanan.get()

    result_window = tk.Toplevel(root)
    result_window.title("Hasil")
    result_window.geometry("300x150")

    result_label = ttk.Label(result_window, text=f"Nama: {nama}\nAlamat: {alamat}\nMakanan Favorit: {makanan_favorit}")
    result_label.pack(padx=10, pady=10)

submit_button = ttk.Button(root, text="Submit", command=submit)

# Menjalankan GUI
root.mainloop()
