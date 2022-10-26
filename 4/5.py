from my_polinom import *

polinom_1 = read_polinom_from_file('polinom-1.txt')
polinom_2 = read_polinom_from_file('polinom-2.txt')
string_to_file('polinom.txt', polinom_to_string(
    sum_polinoms(polinom_1, polinom_2)))
