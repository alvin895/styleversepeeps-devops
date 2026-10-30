import pytest

from app import app, hitung_harga


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_hitung_harga_dengan_diskon():
    hasil = hitung_harga(100000, 20)
    assert hasil == 80000


def test_harga_tidak_boleh_negatif():
    with pytest.raises(ValueError):
        hitung_harga(-100000, 20)


def test_diskon_tidak_boleh_di_bawah_nol():
    with pytest.raises(ValueError):
        hitung_harga(100000, -10)


def test_diskon_tidak_boleh_di_atas_seratus():
    with pytest.raises(ValueError):
        hitung_harga(100000, 110)


def test_endpoint_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_endpoint_harga(client):
    response = client.get("/harga")

    assert response.status_code == 200
    assert response.json["harga_awal"] == 100000
    assert response.json["diskon_persen"] == 20
    assert response.json["harga_akhir"] == 80000