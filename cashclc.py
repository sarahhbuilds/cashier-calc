keranjang = []

while True:
    harga = int(input('masukkan harga: '))

    if harga == 0:
        break
    else:
        keranjang.append(harga)

total_harga = sum(keranjang)

if total_harga > 10000:
    diskon = total_harga * 0.1
    total_bayar = total_harga - diskon
    print('belanja melebihi 10000, anda dapat diskon sebesar 10%')
    print('total yang harus dibayar', total_bayar)
else:
    print('total yang harus dibayar', total_harga)