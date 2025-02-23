#Menghitung faktorial menggunakan rekursi

def faktorial_rekursif(n):

    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif."
    elif n == 0:
        return 1
    else:
        return n * faktorial_rekursif(n-1)

print('\nFaktorial Rekursi 5: ', faktorial_rekursif(5))
print("Faktorial Rekursi 10:", faktorial_rekursif(10))
print('Faktorial Rekursi 4:', faktorial_rekursif (4))
