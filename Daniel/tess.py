# Fungsi untuk menghitung turunan numerik
def numeric_derivative(f, x, h):
    return (f(x + h) - f(x)) / h

# Mendefinisikan fungsi f(x)
def f(x):
    a = 1
    b = 6
    c = 1
    return a*x**2 + b*x - c*x

# Nilai x
x = 1

# Nilai h untuk berbagai tingkat presisi
h1 = 0.1
h2 = 0.001
h3 = 0.00001

# Menghitung turunan menggunakan berbagai tingkat presisi
f_prime_h1 = numeric_derivative(f, x, h1)
f_prime_h2 = numeric_derivative(f, x, h2)
f_prime_h3 = numeric_derivative(f, x, h3)

# Menampilkan hasil
print("Turunan f'(x) dengan h = 0.1:", f_prime_h1)
print("Turunan f'(x) dengan h = 0.001:", f_prime_h2)
print("Turunan f'(x) dengan h = 0.00001:",f_prime_h3)