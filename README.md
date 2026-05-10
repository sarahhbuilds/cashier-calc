# Project Cashier Calculator Simplified

# STRUKTUR PROGRAM
1. py melihat keranjang kosong
2. py melihat while loop dengan kondisi dan juga var berisi input, lalu py print input nya
3. user ketik angka 0, py break while loop
4. semua angka yang terkumpul di var keranjang yg telah terisi angka, akan di jumlahkan dan ditaruh hasilnya di var total harga
5. kondisi baru if, jika lebih dari 10k, akan mendapat diskon
6. else, akan langsung print total harga yang harus dibayar

- keranjang = [] >> buat variable keranjang dengan tipe data collection list yang kosong, untuk menaruh harga barang

- while True: >> digunakan untuk mengulang sebuah proses sampai suatu kondisi terpenuhi
    harga = int(input('masukkan harga: ')) >> buat variable untuk memasukkan harga

    if harga == 0: >> jika user masukkan angka 0, loop akan berhenti
        break
    else: >> selain 0, semau angka yang dimasukkan user akan ditaro di var keranjang
        keranjang.append(harga)

- total_harga = sum(keranjang) >> untuk menaruh hasil penjumlahan dari var keranjang

- if total_harga > 10000: >> jika total harga lebih dari 10ribu, akan mendapat diskon 10%
    diskon = total_harga * 0.1 >> total harga x 0.1 yg adalah 10% dari 100%
    total_bayar = total_harga - diskon >> operasi pengurangan harga dengan diskon, dimasukkan di var total bayar
    print('belanja melebihi 10000, anda dapat diskon sebesar 10%')
    print('total yang harus dibayar', total_bayar) >> print total bayar, dan panggil var total bayar
- else: >> jika tidak lebih dari 10rb, akan print total yang harus dibayar dan var total harga akan dipanggil 
    print('total yang harus dibayar', total_harga)
