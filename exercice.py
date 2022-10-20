#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_bill(name, data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2
    st = 0
    for n in data:
        st += n[INDEX_QUANTITY] * n[INDEX_PRICE]
    taxes = st * (15 / 100)
    T = st + taxes
    Facture = [
        ('SOUS-TOTAL   ', st),
        ('TAXES        ', taxes),
        ("TOTAL        ", T)]
    result = name
    for f in Facture:
        result += "\n" + f"{f[0]} {f[1]}$"

    return result


def format_number(number, num_decimal_digits):
    deci = abs(number) % 1
    Entier = int(abs(number))

    str_deci=str(int(round(deci*10**num_decimal_digits)))
    str_deci="." + str_deci

    str_entier = ''
    while Entier > 1000:
        digits = Entier % 1000
        strdigits = str(digits)
        Entier //= 1000
        str_entier = strdigits +str_entier

    return ('-' if number < 0 else '')+str(Entier)+' '+str_entier+str_deci


def get_triangle(num_rows):
    n=num_rows*2+1
    m=1
    liste='+'*(n)
    for i in range(num_rows):

        liste+='\n'+'+'+' '*(n//2-1) +'A'*(m)+' '*(n//2-1)+'+'
        n-=2
        m+=2

    return liste+'\n'+'+'*(num_rows*2+1)


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 3))

    print(get_triangle(2))
    print(get_triangle(5))
