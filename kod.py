def dodawanie(a, b):
    return a + b


def pomoc():
    print('To jest program kalkulator w wersji 0.1. \n\nWypisuje on sumę dwóch zadanych liczb.')

pomoc()
a = int(input('Wprowadź pierwszą liczbę: '))
b = int(input('Wprowadź drugą liczbę: '))
print('Wynik to', dodawanie(a, b))

