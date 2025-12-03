# app.py
def login(username, password):
    """
    Fungsi simulasi login API.
    Mengembalikan True jika username dan password cocok (misalnya 'admin', 'pass123').
    """
    if username == "admin" and password == "pass123":
        return True
    return False

def penjumlahan(a, b):
    """Fungsi sederhana untuk menguji operasi penjumlahan."""
    return a + b
