#menghitung faktorial menggunakan iteratif

def faktorial_iteratif(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif."
    elif n == 0:
        return 1
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
        return hasil

print('\nFaktorial Iteratif 5: ',faktorial_iteratif(5))
print("Faktorial Iteratif 10:", faktorial_iteratif(10))
print('Faktorial Iteratif 4:', faktorial_iteratif(4))