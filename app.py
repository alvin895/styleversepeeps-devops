
def hitung_harga(harga, diskon):
    if harga < 0:
        raise ValueError("Harga tidak boleh negatif")

    if diskon < 0 or diskon > 100:
        raise ValueError("Diskon harus antara 0 dan 100")

    harga_akhir = harga * (1 - diskon / 100)
    return harga_akhir


if __name__ == "__main__":
    harga_awal = 100000
    diskon = 20

    hasil = hitung_harga(harga_awal, diskon)
    print(f"Harga awal: Rp{harga_awal}")
    print(f"Diskon: {diskon}%")
    print(f"Harga akhir: Rp{hasil:.0f}")
