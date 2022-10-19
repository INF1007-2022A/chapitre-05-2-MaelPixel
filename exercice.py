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
        ('SOUS-TOTAL   ' , st),
        ('TAXES        ' , taxes),
        ("TOTAL        " , T)]
    result=name
    for f in Facture:
        result+= "\n" + f"{f[0]} {f[1]}$"

    return result


def format_number(number, num_decimal_digits):
    return


def get_triangle(num_rows):
    return ""


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
