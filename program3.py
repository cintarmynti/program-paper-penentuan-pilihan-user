import tkinter as tk
from tkinter import messagebox
import pandas as pd

nama_file_excel = 'data_normalisasi.xlsx'
dataframe = pd.read_excel(nama_file_excel)

root = None
harga_awal_entry = None
harga_akhir_entry = None
ukuran_layar_entry = None
resolusi_layar_entry = None
harga_all_entry = None
ukuran_layar_all_entry = None
resolusi_layar_all_entry = None

def filter_berdasarkan_all(harga, ukuran, resolusi):
    harga_all = float(harga)
    ukuran_layar_all = float(ukuran)
    resolusi_layar_all = resolusi

    # Memisahkan nilai lebar dan tinggi resolusi layar dari input pengguna
    lebar_resolusi_layar, tinggi_resolusi_layar = map(int, resolusi_layar_all.split('x'))

    # Memisahkan nilai lebar dan tinggi resolusi layar dari string di dalam DataFrame
    dataframe['resolusi_layar_lebar'], dataframe['resolusi_layar_tinggi'] = zip(*dataframe['resolusi_layar'].str.split('x').apply(lambda x: [int(i) for i in x]))

    # Memilih baris dengan kriteria yang dimasukkan pengguna
    hasil_filter = dataframe.loc[(dataframe['harga'] == harga_all) & 
                                  (dataframe['ukuran_layar'] == ukuran_layar_all) &
                                  (dataframe['resolusi_layar_lebar'] == lebar_resolusi_layar) &
                                  (dataframe['resolusi_layar_tinggi'] == tinggi_resolusi_layar)]

    return hasil_filter  # Mengembalikan DataFrame hasil filter


def filter_berdasarkan_harga(harga_awal, harga_akhir):
    hasil_filter = dataframe.loc[(dataframe['harga'] >= harga_awal) & 
                                 (dataframe['harga'] <= harga_akhir), 
                                 ['nama', 'harga', 'ukuran_layar', 'resolusi_layar']]

    if not hasil_filter.empty:
        return hasil_filter
    else:
        return pd.DataFrame(columns=['nama', 'harga', 'ukuran_layar', 'resolusi_layar'])

def filter_berdasarkan_ukuran(ukuran_layar):
    ukuran_layar = float(ukuran_layar_entry.get("1.0", tk.END).strip())

    hasil_filter = dataframe.loc[dataframe['ukuran_layar'] == ukuran_layar]

    if not hasil_filter.empty:
        return hasil_filter
    else:
        return pd.DataFrame(columns=['nama', 'harga', 'ukuran_layar', 'resolusi_layar'])

def filter_berdasarkan_resolusi(resolusi_layar):
    lebar_resolusi_layar, tinggi_resolusi_layar = map(int, resolusi_layar.split('x'))

    # Memisahkan nilai lebar dan tinggi resolusi layar dari string di dalam DataFrame
    dataframe['resolusi_layar_lebar'], dataframe['resolusi_layar_tinggi'] = zip(*dataframe['resolusi_layar'].str.split('x').apply(lambda x: [int(i) for i in x]))

    # Memilih baris dengan kriteria yang dimasukkan pengguna
    hasil_filter = dataframe.loc[(dataframe['resolusi_layar_lebar'] == lebar_resolusi_layar) &
                                 (dataframe['resolusi_layar_tinggi'] == tinggi_resolusi_layar)]
    
    if not hasil_filter.empty:
        return hasil_filter
    else:
        return pd.DataFrame(columns=['nama', 'harga', 'ukuran_layar', 'resolusi_layar'])


def tampilkan_hasil_filter(hasil_filter):
    result_window = tk.Toplevel(root)
    result_window.title("Hasil Filter")

    # Mendapatkan ukuran layar
    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()

    # Mengatur ukuran jendela menjadi 90% dari ukuran layar
    window_width = int(screen_width * 0.98)
    window_height = int(screen_height * 0.95)
    result_window.geometry(f"{window_width}x{window_height}")

    result_label = ttk.Label(result_window, text="Hasil Filter:", font=("Helvetica", 14))
    result_label.pack(pady=10)

    result_frame = ttk.Frame(result_window)
    result_frame.pack(padx=10, pady=5, fill="both", expand=True)

    result_text = tk.Text(result_frame, width=60, height=15, font=("Helvetica", 12))
    result_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    result_text.config(yscrollcommand=scrollbar.set)

    for index, row in hasil_filter.iterrows():
        row['resolusi_layar'] = row['resolusi_layar'].replace(',', 'x')
        result_text.insert(tk.END, f"Nama Produk: {row['nama']}\nHarga: {row['harga']}\nUkuran Layar: {row['ukuran_layar']}\nResolusi Layar: {row['resolusi_layar']}\n\n")

    # Konfigurasi agar widget bisa mereposisi saat jendela diubah ukurannya
    result_frame.grid_rowconfigure(0, weight=1)
    result_frame.grid_columnconfigure(0, weight=1)





def process_input():
    global harga_awal_entry, harga_akhir_entry, ukuran_layar_entry, resolusi_layar_entry, harga_all_entry, ukuran_layar_all_entry, resolusi_layar_all_entry

    pilihan = entry.get("1.0", "end-1c")
    
    if pilihan == '1':
        # Membuat jendela baru
        filter_window = tk.Toplevel(root)
        filter_window.title("Filter berdasarkan all")

        # Label dan entri untuk harga
        harga_all_label = tk.Label(filter_window, text="Harga :")
        harga_all_label.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        harga_all_entry = tk.Entry(filter_window)
        harga_all_entry.grid(row=0, column=1, padx=20, pady=5)

        # Label dan entri untuk ukuran layar
        ukuran_layar_all_label = tk.Label(filter_window, text="Ukuran Layar:")
        ukuran_layar_all_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        ukuran_layar_all_entry = tk.Entry(filter_window)
        ukuran_layar_all_entry.grid(row=1, column=1, padx=20, pady=5)

        # Label dan entri untuk resolusi layar
        resolusi_layar_all_label = tk.Label(filter_window, text="Resolusi Layar:")
        resolusi_layar_all_label.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        resolusi_layar_all_entry = tk.Entry(filter_window)
        resolusi_layar_all_entry.grid(row=2, column=1, padx=20, pady=5)

        def apply_filter():
            # Mendapatkan nilai dari entri
            harga = harga_all_entry.get()
            ukuran = ukuran_layar_all_entry.get()
            resolusi = resolusi_layar_all_entry.get()

            # Memanggil fungsi filter dan menampilkan hasil
            hasil_filter = filter_berdasarkan_all(harga, ukuran, resolusi)
            tampilkan_hasil_filter(hasil_filter)

        # Tombol untuk menerapkan filter
        apply_button = tk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=3, columnspan=2, padx=20, pady=5)


    elif pilihan == '2':

        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Berdasarkan Harga")
        filter_window.geometry("600x320")

        label_intro = ttk.Label(filter_window, text="Filter Monitor Berdasarkan Harga", font=("Helvetica", 14))
        label_intro.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

        # Menempatkan label_intro di tengah window secara horizontal
        filter_window.grid_columnconfigure(0, weight=1)
        filter_window.grid_rowconfigure(0, weight=1)

        harga_awal_label = ttk.Label(filter_window, text="Masukkan Harga Awal : ")
        harga_awal_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        harga_awal_entry = tk.Text(filter_window, height=3, font=("Helvetica", 12))
        harga_awal_entry.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        harga_akhir_label = ttk.Label(filter_window, text="Masukkan Harga Akhir : ")
        harga_akhir_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        harga_akhir_entry = tk.Text(filter_window, height=3, font=("Helvetica", 12))
        harga_akhir_entry.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        def apply_filter():
            harga_awal = float(harga_awal_entry.get("1.0", "end-1c"))
            harga_akhir = float(harga_akhir_entry.get("1.0", "end-1c"))
            hasil_filter = filter_berdasarkan_harga(harga_awal, harga_akhir) 
            tampilkan_hasil_filter(hasil_filter)

        apply_button = ttk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=5, column=0, padx=20, pady=(10, 20), sticky="ew")

        # Menentukan panjang label_intro agar mengisi seluruh lebar jendela
        filter_window.update_idletasks()
        label_intro.config(width=filter_window.winfo_width())




    elif pilihan == '3':

        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Berdasarkan Ukuran Layar")
        filter_window.geometry("600x320")

        label_intro = ttk.Label(filter_window, text="Filter Monitor Berdasarkan Resolusi", font=("Helvetica", 14))
        label_intro.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

        ukuran_layar_label = ttk.Label(filter_window, text="Masukkan Ukuran Layar Yang Di Inginkan : ")
        ukuran_layar_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        ukuran_layar_entry = tk.Text(filter_window, height=3, font=("Helvetica", 12))
        ukuran_layar_entry.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        def apply_filter():
            ukuran_layar = ukuran_layar_entry.get("1.0", tk.END).strip()
            hasil_filter = filter_berdasarkan_ukuran(ukuran_layar)
            tampilkan_hasil_filter(hasil_filter)

        apply_button = ttk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=3, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ew")

        # Konfigurasi agar kolom dan baris jendela menyesuaikan konten
        filter_window.grid_columnconfigure(0, weight=1)
        filter_window.grid_columnconfigure(1, weight=1)
        filter_window.grid_rowconfigure(0, weight=1)
        filter_window.grid_rowconfigure(1, weight=1)
        filter_window.grid_rowconfigure(2, weight=1)
        filter_window.grid_rowconfigure(3, weight=1)

        

    elif pilihan == '4':
        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Berdasarkan Resolusi Layar")
        filter_window.geometry("600x320")

        label_intro = ttk.Label(filter_window, text="Filter Monitor Berdasarkan Resolusi", font=("Helvetica", 14))
        label_intro.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

        resolusi_layar_label = ttk.Label(filter_window, text="Resolusi Layar (contoh: 1920x1080):")
        resolusi_layar_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        resolusi_layar_entry = tk.Text(filter_window, height=3, font=("Helvetica", 12))
        resolusi_layar_entry.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        def apply_filter():
            resolusi_layar = resolusi_layar_entry.get("1.0", tk.END).strip()
            hasil_filter = filter_berdasarkan_resolusi(resolusi_layar)
            tampilkan_hasil_filter(hasil_filter)

        apply_button = ttk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=3, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ew")

        # Konfigurasi agar kolom dan baris jendela menyesuaikan konten
        filter_window.grid_columnconfigure(0, weight=1)
        filter_window.grid_columnconfigure(1, weight=1)
        filter_window.grid_rowconfigure(0, weight=1)
        filter_window.grid_rowconfigure(1, weight=1)
        filter_window.grid_rowconfigure(2, weight=1)
        filter_window.grid_rowconfigure(3, weight=1)


import tkinter as tk
from tkinter import ttk


def main():
    global root, entry, label_result
    root = tk.Tk()
    root.title("Program Rekomendasi Monitor")
    root.geometry("600x320")

    style = ttk.Style()
    style.theme_use("clam")  # Ganti dengan tema yang diinginkan

    label_intro = ttk.Label(root, text="Selamat Datang di Program Rekomendasi Monitor", font=("Helvetica", 14))
    label_intro.pack(pady=10)

    options_frame = ttk.Frame(root)
    options_frame.pack(pady=10)

    label_options = ttk.Label(options_frame, text="Pilihan:\n1: Filter harga, ukuran layar, dan resolusi\n2: Filter harga\n3: Filter ukuran layar\n4: Filter resolusi layar", justify="left", wraplength=200)
    
    label_options.grid(row=0, column=0, padx=10)

    entry = tk.Text(options_frame, width=30, height=10, font=("Helvetica", 12))
    entry.grid(row=0, column=1, padx=10, pady=5)

    button_process = ttk.Button(root, text="Proses", command=process_input)
    button_process.pack(pady=10)

    label_result = ttk.Label(root, text="")
    label_result.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
