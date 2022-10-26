from my_polinom import *

k = int(input('Введите целочисленное значение для k: '))

print(f'k={k} => {polinom_to_string(random_polinom(k))}' +
      f' или {polinom_to_string(random_polinom(k))}' +
      f' или {polinom_to_string(random_polinom(k))}')
string_to_file('polinom.txt', polinom_to_string(random_polinom(k)))
