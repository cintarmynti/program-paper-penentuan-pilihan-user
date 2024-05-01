import tkinter as tk
from tkinter import messagebox

# Deklarasi variabel global
root = None
entry = None

def filter_berdasarkan_harga_ukuran_resolusi():
    # Fungsi untuk filter berdasarkan harga, ukuran layar, dan resolusi layar
    # Implementasi logika filtering di sini
    
    # Sementara, untuk contoh, kembalikan hasil dummy
    return ["Monitor 1", "Monitor 2", "Monitor 3"]

def tampilkan_hasil_filter(hasil_filter):
    # Fungsi untuk menampilkan hasil filter
    result_window = tk.Toplevel(root)
    result_window.title("Hasil Filter")
    
    result_label = tk.Label(result_window, text="Hasil Filter:")
    result_label.pack()
    
    result_text = tk.Text(result_window, width=40, height=10)
    result_text.pack()
    
    for item in hasil_filter:
        result_text.insert(tk.END, f"{item}\n")

def process_input():
    global entry  # Mengakses variabel entry yang dideklarasikan sebagai global
    
    pilihan = entry.get("1.0", "end-1c")
    if pilihan == '1':
        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Harga, Ukuran Layar, dan Resolusi")
        
        # Label Harga
        harga_label = tk.Label(filter_window, text="Harga:")
        harga_label.grid(row=0, column=0, sticky="w", padx=20, pady=5)  # Menempatkan label di bagian kiri atas
        
        # Input Harga
        harga_entry = tk.Entry(filter_window)
        harga_entry.grid(row=1, column=0, padx=20, pady=5)  # Menempatkan input di bawah label
        
        # Label Ukuran Layar
        ukuran_label = tk.Label(filter_window, text="Ukuran Layar (inch):")
        ukuran_label.grid(row=2, column=0, sticky="w", padx=20, pady=5)  # Menempatkan label di bagian kiri atas
        
        # Input Ukuran Layar
        ukuran_entry = tk.Entry(filter_window)
        ukuran_entry.grid(row=3, column=0, padx=20, pady=5)  # Menempatkan input di bawah label
        
        # Label Resolusi Layar
        resolusi_label = tk.Label(filter_window, text="Resolusi Layar (contoh: 1920x1080):")
        resolusi_label.grid(row=4, column=0, sticky="w", padx=20, pady=5)  # Menempatkan label di bagian kiri atas
        
        # Input Resolusi Layar
        resolusi_entry = tk.Entry(filter_window)
        resolusi_entry.grid(row=5, column=0, padx=20, pady=5)  # Menempatkan input di bawah label
        
        def apply_filter():
            harga = float(harga_entry.get())
            ukuran_layar = float(ukuran_entry.get())
            resolusi = resolusi_entry.get()
        
            # Memeriksa apakah format resolusi sesuai
            resolusi_parts = resolusi.split('x')
            if len(resolusi_parts) != 2:
                messagebox.showerror("Error", "Format resolusi tidak valid. Gunakan format lebar x tinggi (misal: 1920x1080)")
                return
            
            # Memeriksa apakah kedua bagian adalah angka
            try:
                lebar_resolusi_layar, tinggi_resolusi_layar = map(int, resolusi_parts)
            except ValueError:
                messagebox.showerror("Error", "Format resolusi tidak valid. Gunakan format lebar x tinggi (misal: 1920x1080)")
                return
            
            # Panggil fungsi filter
            hasil_filter = filter_berdasarkan_harga_ukuran_resolusi()
            tampilkan_hasil_filter(hasil_filter)
        
        # Button Terapkan Filter
        apply_button = tk.Button(filter_window, text="Terapkan Filter", command=apply_filter)
        apply_button.grid(row=6, columnspan=2, padx=20, pady=5)  # Menempatkan tombol di bawah input
        
    elif pilihan == '2':
        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Harga")
        
        # Label Harga Awal
        harga_awal_label = tk.Label(filter_window, text="Harga Awal:")
        harga_awal_label.grid(row=0, column=0, sticky="w", padx=20, pady=5)  # Menempatkan label di bagian kiri atas
        
        # Input Harga Awal
        harga_awal_entry = tk.Entry(filter_window)
        harga_awal_entry.grid(row=0, column=1, padx=20, pady=5)  # Menempatkan input di bawah label
        
        # Label Harga Akhir
        harga_akhir_label = tk.Label(filter_window, text="Harga Akhir:")
        harga_akhir_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)  # Menempatkan label di bagian kiri atas
        
        # Input Harga Akhir
        harga_akhir_entry = tk.Entry(filter_window)
        harga_akhir_entry.grid(row=1, column=1, padx=20, pady=5)  # Menempatkan input di bawah label
        
        # Button Terapkan Filter
        apply_button = tk.Button(filter_window, text="Terapkan Filter", command=filter_berdasarkan_harga)
        apply_button.grid(row=2, columnspan=2, padx=20, pady=5)  # Menempatkan tombol di bawah input



def main():
    global root, entry  # Deklarasi root dan entry sebagai variabel global
    root = tk.Tk()
    root.title("Program Rekomendasi Monitor")
    
    label_intro = tk.Label(root, text="Selamat Datang di Program Rekomendasi Monitor", font=("Helvetica", 14))
    label_intro.grid(row=0, column=0, columnspan=2, pady=10)

    label_options = tk.Label(root, text="Pilihan:\n1: Filter harga, ukuran layar, dan resolusi\n2: Filter harga\n3: Filter ukuran layar\n4: Filter resolusi layar", justify="left")
    label_options.grid(row=1, column=0, padx=10)

    entry = tk.Text(root, width=30, height=5, font=("Helvetica", 12))  # Mengatur width, height, dan font size
    entry.grid(row=1, column=1, padx=10)

    button_process = tk.Button(root, text="Proses", command=process_input)
    button_process.grid(row=2, column=0, columnspan=2, pady=10)

    label_result = tk.Label(root, text="")
    label_result.grid(row=3, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
