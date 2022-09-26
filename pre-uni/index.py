#!/usr/bin/env python3
from fractions import Fraction
import math


# def decimal_to_fraction(whole, decimal, repeat):
#     full_num = "{0}{1}{2}".format(whole, decimal, int(str(repeat)*10))
#     tens = 10 ** len(str(decimal)+str(repeat)*10)
#     GCD = math.gcd(int(full_num), tens)

#     first_half = "{0}/{1}".format(int(int(full_num) / GCD), int(tens / GCD))


# myInput = input("enter ur input: ").split(",")
# print(decimal_to_fraction(myInput[0], myInput[1], myInput[2]))


def dec(whole, decimal, repeat):
    res = Fraction("{0}.{1}{2}".format(
        whole, decimal, str(repeat)*10)).limit_denominator()

    numerator, denominator = str(res).split("/")
    return "{0}/{1}".format(numerator*10//10, denominator*10//10)


def decimal_to_fraction(input_string):
    [whole, decimal, repeating] = input_string.split(",")

    res = Fraction("{0}.{1}{2}".format(
        whole, decimal, str(repeating)*10)).limit_denominator()

    frac = str(res).split("/")

    numerator = frac[0]
    denominator = frac[1] if len(frac) == 2 else 1

    return "{0} / {1}".format(int(numerator)*10//10, int(denominator)*10//10)


assert decimal_to_fraction("7,,0") == "7 / 1"
assert decimal_to_fraction("0,,0") == "0 / 1"
assert decimal_to_fraction("0,5,0") == "1 / 2"
assert decimal_to_fraction("0,08,3") == "1 / 12"
assert decimal_to_fraction("0,02,27") == "1 / 44"
assert decimal_to_fraction("123,456,789") == "41111111 / 333000"
assert decimal_to_fraction("987,,987") == "329000 / 333"


myInput = input("enter ur input: ").split(",")
print(dec(myInput[0], myInput[1], myInput[2]))
