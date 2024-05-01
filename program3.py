import tkinter as tk

def filter_berdasarkan_harga_ukuran_resolusi():
    # Fungsi untuk filter berdasarkan harga, ukuran layar, dan resolusi layar
    pass

def filter_berdasarkan_harga():
    # Fungsi untuk filter berdasarkan harga
    pass

def filter_berdasarkan_ukuran_layar():
    # Fungsi untuk filter berdasarkan ukuran layar
    pass

def filter_berdasarkan_resolusi_layar():
    # Fungsi untuk filter berdasarkan resolusi layar
    pass

def tampilkan_hasil_filter(hasil_filter):
    # Fungsi untuk menampilkan hasil filter
    pass

def process_input():
    pilihan = entry.get("1.0", "end-1c")
    if pilihan == '1':
        hasil_filter = filter_berdasarkan_harga_ukuran_resolusi()
        tampilkan_hasil_filter(hasil_filter)
    elif pilihan == '2':
        hasil_filter = filter_berdasarkan_harga()
        tampilkan_hasil_filter(hasil_filter)
    elif pilihan == '3':
        hasil_filter = filter_berdasarkan_ukuran_layar()
        tampilkan_hasil_filter(hasil_filter)
    elif pilihan == '4':
        hasil_filter = filter_berdasarkan_resolusi_layar()
        tampilkan_hasil_filter(hasil_filter)
    else:
        label_result.config(text="Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")

def main():
    root = tk.Tk()
    root.title("Program Rekomendasi Monitor")
    
    label_intro = tk.Label(root, text="Selamat Datang di Program Rekomendasi Monitor", font=("Helvetica", 14))
    label_intro.grid(row=0, column=0, columnspan=2, pady=10)

    label_options = tk.Label(root, text="Pilihan:\n1: Filter harga, ukuran layar, dan resolusi\n2: Filter harga\n3: Filter ukuran layar\n4: Filter resolusi layar", justify="left")
    label_options.grid(row=1, column=0, padx=10)

    entry = tk.Text(root, width=50, height=5, font=("Helvetica", 12))  # Mengatur width, height, dan font size
    entry.grid(row=1, column=1, padx=10)

    button_process = tk.Button(root, text="Proses", command=process_input)
    button_process.grid(row=2, column=0, columnspan=2, pady=10)

    label_result = tk.Label(root, text="")
    label_result.grid(row=3, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
