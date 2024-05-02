import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Nama file Excel yang ingin Anda baca
nama_file_excel = 'data_normalisasi.xlsx'
dataframe = pd.read_excel(nama_file_excel)

#--------------------------------------------------------------------------



def filter_berdasarkan_harga_ukuran_resolusi():
    harga = float(input("Masukkan harga: "))

    # Mengonversi input ukuran layar menjadi float dengan menangani kemungkinan error
    while True:
        ukuran_layar_input = input("Masukkan ukuran layar (dalam inch, gunakan koma jika desimal): ")  # Input ukuran layar dalam bentuk string
        try:
            # Mengganti koma dengan titik jika ada
            ukuran_layar_input = ukuran_layar_input.replace(',', '.')
            ukuran_layar = float(ukuran_layar_input)  # Konversi input ukuran layar menjadi float
            break  # Jika konversi berhasil, keluar dari loop
        except ValueError:
            print("Input ukuran layar harus berupa angka. Silakan coba lagi.")

    # Meminta input untuk resolusi layar dalam format "1920x1080"
    resolusi_layar_input = input("Masukkan resolusi layar (contoh: 1920x1080): ")

    # Memisahkan nilai lebar dan tinggi resolusi layar dari input pengguna
    lebar_resolusi_layar, tinggi_resolusi_layar = map(int, resolusi_layar_input.split('x'))

    # Memisahkan nilai lebar dan tinggi resolusi layar dari string di dalam DataFrame
    dataframe['resolusi_layar_lebar'], dataframe['resolusi_layar_tinggi'] = zip(*dataframe['resolusi_layar'].str.split(',').apply(lambda x: [int(i) for i in x]))

    # Memilih baris dengan kriteria yang dimasukkan pengguna
    hasil_filter = dataframe.loc[(dataframe['harga'] == harga) & 
                                  (dataframe['ukuran_layar'] == ukuran_layar) &
                                  (dataframe['resolusi_layar_lebar'] == lebar_resolusi_layar) &
                                  (dataframe['resolusi_layar_tinggi'] == tinggi_resolusi_layar), 'nama']

    return hasil_filter

def filter_berdasarkan_harga():
    harga_awal = float(input("Masukkan harga awal: "))
    harga_akhir = float(input("Masukkan harga akhir: "))

    hasil_filter = dataframe.loc[(dataframe['harga'] >= harga_awal) & 
                                 (dataframe['harga'] <= harga_akhir), 
                                 ['nama', 'harga', 'ukuran_layar', 'resolusi_layar']]

    # Check if any rows match the given criteria
    if not hasil_filter.empty:
        # If there are matching rows, retrieve and display the product information
        print("Produk dengan harga antara", harga_awal, "dan", harga_akhir, "adalah:")
        for index, row in hasil_filter.iterrows():
            row['resolusi_layar'] = row['resolusi_layar'].replace(',', 'x')
            print("Nama Produk:", row['nama'])
            print("Harga:", row['harga'])
            print("Ukuran Layar:", row['ukuran_layar'])
            print("Resolusi Layar:", row['resolusi_layar'])
            print()  # Baris kosong untuk pemisah antar produk
    else:
        print("Tidak ada produk dengan harga antara", harga_awal, "dan", harga_akhir)

def filter_berdasarkan_ukuran_layar():
    ukuran_layar_input = float(input("Masukkan ukuran layar (dalam inch): "))  # Meminta input ukuran layar
    
    # Memilih baris dengan kriteria yang dimasukkan pengguna
    hasil_filter = dataframe.loc[dataframe['ukuran_layar'] == ukuran_layar_input]

    # Check if
        # Check if any rows match the given criteria
    if not hasil_filter.empty:
        # If there are matching rows, retrieve and display the product information
        print("Produk dengan ukuran layar", ukuran_layar_input, "adalah:")
        for index, row in hasil_filter.iterrows():
            # Replace ',' with 'x' in resolusi_layar column
            row['resolusi_layar'] = row['resolusi_layar'].replace(',', 'x')
            
            print("Nama Produk:", row['nama'])
            print("Ukuran Layar:", row['ukuran_layar'])
            print("Harga:", row['harga'])
            print("Resolusi Layar:", row['resolusi_layar'])
            print()  # Baris kosong untuk pemisah antar produk
    else:
        print("Tidak ada produk dengan ukuran layar", ukuran_layar_input)


def filter_berdasarkan_resolusi_layar():
    resolusi_layar_input = input("Masukkan resolusi layar (contoh: 1920x1080): ")
    # Memisahkan nilai lebar dan tinggi resolusi layar dari input pengguna
    lebar_resolusi_layar, tinggi_resolusi_layar = map(int, resolusi_layar_input.split('x'))

    # Memisahkan nilai lebar dan tinggi resolusi layar dari string di dalam DataFrame
    dataframe['resolusi_layar_lebar'], dataframe['resolusi_layar_tinggi'] = zip(*dataframe['resolusi_layar'].str.split('x').apply(lambda x: [int(i) for i in x]))

    # Memilih baris dengan kriteria yang dimasukkan pengguna
    hasil_filter = dataframe.loc[(dataframe['resolusi_layar_lebar'] == lebar_resolusi_layar) &
                                 (dataframe['resolusi_layar_tinggi'] == tinggi_resolusi_layar)]

    if not hasil_filter.empty:
        print("Produk dengan resolusi layar", resolusi_layar_input, "adalah:")
        for index, row in hasil_filter.iterrows():
            print("Nama Produk:", row['nama'])
            print("Ukuran Layar:", row['ukuran_layar'])
            print("Harga:", row['harga'])
            print("Resolusi Layar:", row['resolusi_layar'])
            print()  # Baris kosong untuk pemisah antar produk
    else:
        print("Tidak ada produk dengan resolusi layar", resolusi_layar_input)


def tampilkan_hasil_filter(hasil_filter):
    if hasil_filter is None or hasil_filter.empty:
        print("Tidak ada produk dengan kriteria yang ditentukan.")
    else:
        print(hasil_filter)



def main():
    print("============ Selamat Datang di Program Rekomendasi Monitor ============")
    print("Pilihan 1: Filter berdasarkan harga, ukuran layar, dan resolusi layar")
    print("Pilihan 2: Filter berdasarkan harga")
    print("Pilihan 3: Filter berdasarkan ukuran layar")
    print("Pilihan 4: Filter berdasarkan resolusi layar")

    pilihan = input("Masukkan pilihan Anda: ")

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
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, 4, atau 5.")

if __name__ == "__main__":
    main()
