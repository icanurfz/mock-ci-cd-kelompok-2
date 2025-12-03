# test_app.py
from app import login, penjumlahan

# Uji fungsi login
def test_login_sukses():
    assert login("admin", "pass123")

def test_login_gagal():
    assert login("user", "salah") == False

# Uji fungsi penjumlahan
def test_penjumlahan_positif():
    assert penjumlahan(5, 3) == 8

def test_penjumlahan_negatif():
    assert penjumlahan(-1, 1) == 0
