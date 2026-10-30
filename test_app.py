import pytest

from app import hitung_harga


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