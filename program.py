import tkinter as tk
from tkinter import ttk

def process_input():
    global harga_awal_entry, harga_akhir_entry, ukuran_layar_entry, resolusi_layar_entry, harga_all_entry, ukuran_layar_all_entry, resolusi_layar_all_entry, combo

    pilihan = combo.get()
    
    if pilihan == '1':
        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Berdasarkan Semua")
        filter_window.geometry("600x360")

        label_intro = ttk.Label(filter_window, text="Filter Berdasarkan Semua", font=("Helvetica", 14))
        label_intro.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

        # Menempatkan label_intro di tengah window secara horizontal
        filter_window.grid_columnconfigure(0, weight=1)
        filter_window.grid_rowconfigure(0, weight=1)

        harga_all_label = ttk.Label(filter_window, text="Masukkan Harga  : ")
        harga_all_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        harga_all_entry = tk.Text(filter_window, height=1.5, font=("Helvetica", 12))
        harga_all_entry.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        ukuran_layar_label = ttk.Label(filter_window, text="Masukkan Ukuran Layar : ")
        ukuran_layar_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        ukuran_layar_all_entry = tk.Text(filter_window, height=1.5, font=("Helvetica", 12))
        ukuran_layar_all_entry.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        resolusi_layar_label = ttk.Label(filter_window, text="Masukkan Resolusi Layar : ")
        resolusi_layar_label.grid(row=5, column=0, padx=20, pady=5, sticky="w")

        resolusi_layar_entry = tk.Text(filter_window, height=1.5, font=("Helvetica", 12))
        resolusi_layar_entry.grid(row=6, column=0, padx=20, pady=5, sticky="ew")

        def apply_filter():
            # Mendapatkan nilai dari entri
            harga = float(harga_all_entry.get("1.0", "end-1c"))
            ukuran = float(ukuran_layar_all_entry.get("1.0", "end-1c"))
            resolusi = resolusi_layar_entry.get("1.0", tk.END).strip()

            # Memanggil fungsi filter dan menampilkan hasil
            hasil_filter = filter_berdasarkan_all(harga, ukuran, resolusi)
            tampilkan_hasil_filter(hasil_filter)

        apply_button = ttk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=7, column=0, padx=20, pady=(10, 20), sticky="ew")

        # Menentukan panjang label_intro agar mengisi seluruh lebar jendela
        filter_window.update_idletasks()
        label_intro.config(width=filter_window.winfo_width())

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

        label_intro = ttk.Label(filter_window, text="Filter Monitor Berdasarkan Ukuran", font=("Helvetica", 14))
        label_intro.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

        ukuran_layar_label = ttk.Label(filter_window, text="Masukkan Ukuran Layar Yang Diinginkan : ")
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
    
def main():
    global root, combo
    
    root = tk.Tk()
    root.title("Program Filter Monitor")
    root.geometry("300x200")
    
    label_intro = ttk.Label(root, text="Pilih Opsi Filter:", font=("Helvetica", 14))
    label_intro.pack(pady=10)
    
    combo = ttk.Combobox(root, values=["1", "2", "3", "4"])
    combo.pack(pady=10)
    
    button = ttk.Button(root, text="Submit", command=process_input)
    button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
