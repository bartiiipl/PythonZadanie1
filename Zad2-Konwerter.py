#!/usr/bin/env python3

def Konwerter():
    liczba = input("Podaj swoja liczbe calkowita: ")
    liczba = int(liczba)
    return liczba

moja_liczba = Konwerter()
print("Twoja liczba to {}".format(moja_liczba))