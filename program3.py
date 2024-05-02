import tkinter as tk
from tkinter import messagebox
import pandas as pd

nama_file_excel = 'data_normalisasi.xlsx'
dataframe = pd.read_excel(nama_file_excel)

root = None
harga_awal_entry = None
harga_akhir_entry = None

def filter_berdasarkan_harga_ukuran_resolusi(harga, ukuran_layar, resolusi_layar):
    resolusi_parts = resolusi_layar.split('x')

    if len(resolusi_parts) != 2:
        messagebox.showerror("Error", "Format resolusi tidak valid. Gunakan format lebar x tinggi (misal: 1920x1080)")
        return

    try:
        lebar_resolusi_layar, tinggi_resolusi_layar = map(int, resolusi_parts)
    except ValueError:
        messagebox.showerror("Error", "Format resolusi tidak valid. Gunakan format lebar x tinggi (misal: 1920x1080)")
        return

    hasil_filter = dataframe.loc[(dataframe['harga'] == harga) & 
                                  (dataframe['ukuran_layar'] == ukuran_layar) &
                                  (dataframe['resolusi_layar_lebar'] == lebar_resolusi_layar) &
                                  (dataframe['resolusi_layar_tinggi'] == tinggi_resolusi_layar), 'nama']

    if not hasil_filter.empty:
        return hasil_filter.tolist()
    else:
        return ["Tidak ada produk dengan kriteria yang dimasukkan"]

def filter_berdasarkan_harga():
    harga_awal = float(harga_awal_entry.get())
    harga_akhir = float(harga_akhir_entry.get())

    hasil_filter = dataframe.loc[(dataframe['harga'] >= harga_awal) & 
                                 (dataframe['harga'] <= harga_akhir), 
                                 ['nama', 'harga', 'ukuran_layar', 'resolusi_layar']]

    if not hasil_filter.empty:
        return hasil_filter
    else:
        return pd.DataFrame(columns=['nama', 'harga', 'ukuran_layar', 'resolusi_layar'])

def tampilkan_hasil_filter(hasil_filter):
    result_window = tk.Toplevel(root)
    result_window.title("Hasil Filter")

    result_label = tk.Label(result_window, text="Hasil Filter:")
    result_label.pack()

    result_text = tk.Text(result_window, width=40, height=10)
    result_text.pack()

    for index, row in hasil_filter.iterrows():
        row['resolusi_layar'] = row['resolusi_layar'].replace(',', 'x')
        result_text.insert(tk.END, f"Nama Produk: {row['nama']}\nHarga: {row['harga']}\nUkuran Layar: {row['ukuran_layar']}\nResolusi Layar: {row['resolusi_layar']}\n\n")

def process_input():
    global harga_awal_entry, harga_akhir_entry

    pilihan = entry.get("1.0", "end-1c")
    if pilihan == '1':
        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Harga, Ukuran Layar, dan Resolusi")
        
        harga_awal_label = tk.Label(filter_window, text="Harga Awal:")
        harga_awal_label.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        harga_awal_entry = tk.Entry(filter_window)
        harga_awal_entry.grid(row=0, column=1, padx=20, pady=5)
        
        harga_akhir_label = tk.Label(filter_window, text="Harga Akhir:")
        harga_akhir_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        harga_akhir_entry = tk.Entry(filter_window)
        harga_akhir_entry.grid(row=1, column=1, padx=20, pady=5)
        
        def apply_filter():
            harga_awal = float(harga_awal_entry.get())
            harga_akhir = float(harga_akhir_entry.get())
            ukuran_layar = float(ukuran_entry.get())
            resolusi = resolusi_entry.get()
        
            resolusi_parts = resolusi.split('x')
            if len(resolusi_parts) != 2:
                messagebox.showerror("Error", "Format resolusi tidak valid. Gunakan format lebar x tinggi (misal: 1920x1080)")
                return
            
            try:
                lebar_resolusi_layar, tinggi_resolusi_layar = map(int, resolusi_parts)
            except ValueError:
                messagebox.showerror("Error", "Format resolusi tidak valid. Gunakan format lebar x tinggi (misal: 1920x1080)")
                return
            
            hasil_filter = filter_berdasarkan_harga_ukuran_resolusi(harga_awal, ukuran_layar, resolusi)
            tampilkan_hasil_filter(hasil_filter)
        
        apply_button = tk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=2, columnspan=2, padx=20, pady=5)

    elif pilihan == '2':
        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Harga")
        
        harga_awal_label = tk.Label(filter_window, text="Harga Awal:")
        harga_awal_label.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        harga_awal_entry = tk.Entry(filter_window)
        harga_awal_entry.grid(row=0, column=1, padx=20, pady=5)
        
        harga_akhir_label = tk.Label(filter_window, text="Harga Akhir:")
        harga_akhir_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        harga_akhir_entry = tk.Entry(filter_window)
        harga_akhir_entry.grid(row=1, column=1, padx=20, pady=5)
        
        def apply_filter():
            harga_awal = float(harga_awal_entry.get())
            harga_akhir = float(harga_akhir_entry.get())
            hasil_filter = filter_berdasarkan_harga() 
            tampilkan_hasil_filter(hasil_filter)
            
        apply_button = tk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=2, columnspan=2, padx=20, pady=5)


def main():
    global root, entry
    root = tk.Tk()
    root.title("Program Rekomendasi Monitor")
    
    label_intro = tk.Label(root, text="Selamat Datang di Program Rekomendasi Monitor", font=("Helvetica", 14))
    label_intro.grid(row=0, column=0, columnspan=2, pady=10)

    label_options = tk.Label(root, text="Pilihan:\n1: Filter harga, ukuran layar, dan resolusi\n2: Filter harga\n3: Filter ukuran layar\n4: Filter resolusi layar", justify="left")
    label_options.grid(row=1, column=0, padx=10)

    entry = tk.Text(root, width=30, height=5, font=("Helvetica", 12))
    entry.grid(row=1, column=1, padx=10)

    button_process = tk.Button(root, text="Proses", command=process_input)
    button_process.grid(row=2, column=0, columnspan=2, pady=10)

    label_result = tk.Label(root, text="")
    label_result.grid(row=3, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
