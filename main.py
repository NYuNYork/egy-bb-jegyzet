import modul as m

# 1. feladat
Kategoriak = m.beolvasas('titanic.txt', 'utf-8')
# 2.feladat
print(f'2.feladat: {len(Kategoriak)} db')
#3.
print(f'3.deladat: {m.osszegzes(Kategoriak)} fő')

# 4. feladat

kulcsszo =input('4.feladat: kulcsszó: ')
van = m.nev_keres(Kategoriak)
if van:
    print('\t van találat')
    #5.
    print('5. feladat:  ')
    m.kulcsszavas_kategoria
else: print('nincs találat')

#6.
print('6.feladat')
megh = m.meghaladta(Kategoriak)
for k in megh:
    k:m.Kategoriak
    print(f'\t{k.nev}')

# 7.
print(f'7.feladat{m.legtöbb_túlélő}')