#!/usr/bin/env python3

class Kwiat:
   def __init__(self, kolor, rodzaj, ilosc_lisci):
       self.kolor = kolor
       self.rodzaj = rodzaj
       self.ilosc_lisci = ilosc_lisci

   def wypisz_informacje(self):
       print("Jestes {} {}, jestes {} lisciowy".format(self.kolor, self.rodzaj, self.ilosc_lisci))

kolor = input("Kolor kwiata: ")
rodzaj = input("Rodzaj kwiata: ")
ilosc_lisci = input("Ilosc lisci: ")

ilosc_lisci = int(ilosc_lisci)

kwiat = Kwiat(kolor, rodzaj, ilosc_lisci)

kwiat.wypisz_informacje()