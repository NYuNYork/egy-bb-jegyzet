from encodings import utf_8
import encodings
import re
from tkinter.tix import Tree


class Kategoriak:
    def __init__(self, sor: str):
        v: list = sor.strip().split(";")
        self.nev = v[0]
        self.tul = int(v[1])
        self.elt = int(v[2])
        self.osz = self.tul + self.elt


def beolvasas(f: str, e: str):
    kategoria = []
    for s in open(file = f, encoding = e):
        Kategoriak.append(kategoria(s))
    return Kategoriak


def osszegzes(ks: list):
    sum = 0
    for k in ks:
        k : Kategoriak
        sum += k.szemely
    return sum


def nev_keres(ks:list, t:str):
    for k in ks:
        if t in k.nev: return True
    return False    


def kulcsszavas_kategoria (ks:list, t:str ):
    for k in ks:
        k:Kategoriak
        if t in k.nev:
            print('\tNincs találat')

def meghaladta(ks:list,):
    val = []
    for k in ks:
        k:Kategoriak
        if k.eltunt > k.szemely*6:
            val.append(k)
        return val


def legtöbb_túlélő(ks:list):
    maxi = 0
    for i in range(1,len(ks)):
        if ks[i].tulelo > ks[maxi].tulelo:
            maxi = i
    return ks[maxi].nev
