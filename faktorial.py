def pangkat_rekrusif(a, n): 
    """
    Args:
    a:Bilangan dasar (angka yang akan dipangkatkan)
    n:pangkat(Bilangan bulat no-negatif)
    Returns: 
    hasil dari a^n.
    """
    if n == 0:
        return 1
    elif n < 0: 
        return 1 / pangkat_rekrusif (a, -n)
    else: 
        return a * pangkat_rekrusif (a, n - 1)
    
a = 3
n = 4
hasil= pangkat_rekrusif(a, n)
print(f"{a}^{n}= {hasil}")

a= 2
n= -4
hasil= pangkat_rekrusif (a, n)
print(f"{a}^{n}= {hasil}")

a= 0
n= -8
hasil= pangkat_rekrusif (a, n)
print(f"{a}^{n}= {hasil}")

