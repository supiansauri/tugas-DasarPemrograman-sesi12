# my_module.py
def count_uppercase(s: str) -> int:
    """
    Menghitung jumlah huruf besar (Upper Case) pada sebuah string s.

    :param s: string yang akan dihitung jumlah huruf besarnya.
    :return: jumlah huruf besar (Upper Case) pada string s.
    """
    return sum(1 for c in s if c.isupper())
