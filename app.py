from flask import Flask, jsonify

app = Flask(__name__)


def hitung_harga(harga, diskon):
    if harga < 0:
        raise ValueError("Harga tidak boleh negatif")

    if diskon < 0 or diskon > 100:
        raise ValueError("Diskon harus antara 0 dan 100")

    harga_akhir = harga * (1 - diskon / 100)
    return harga_akhir


@app.route("/")
def home():
    return jsonify({
        "aplikasi": "StyleversePeeps",
        "status": "running"
    })


@app.route("/harga")
def harga():
    harga_awal = 100000
    diskon = 20

    hasil = hitung_harga(harga_awal, diskon)

    return jsonify({
        "harga_awal": harga_awal,
        "diskon_persen": diskon,
        "harga_akhir": hasil
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)