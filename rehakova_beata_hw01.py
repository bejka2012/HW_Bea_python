# Ahoj opravovateli (Adelko, Marto)!

# Moc me mrzi, ze odevzdavam ukol na posledni chvili a jeste k tomu nespravne. Neni mi to moc podobne. Vetsinou vse delam s predstihem, 
# abych byla v klidu, ze je vse bez zbytecneho stresu a na cas. V pripade tohoto domaciho ukolu jsem vsak uplne v pasti, nevim si rady
# vse je zpusobeno tim, ze je na me moc informaci naraz v kratke dobe a ja jsem po 6 letech nevyuzivani mozku, coz mi ted zivot dava sezrat.
# Nez neco pochopim tak mi to trva neskutecne dlouho. Malinky progress vidim, ale zrejme to neni dostatecne. 
# Bohuzel jsem doted nenasla dostatek casu sednout k pythonu. Prozatim jsem stihla zopakovat Uvod do pythonu (prerekvizitu)
# a 3 online lekce, ktere po zadani mailu na strankach Czechitas lze absolvovat. Je to malo na to, abych vedela, jak spravne napsat podminku
# ktera je potrebna pro spocitani znaku.
# Prosim proto o schovyvavost a nasmerovani k oprave ukolu.
# Moc dekuji predem
# Bea z Karvine

import json

signs = []

with open("alice.txt", encoding="utf-8") as a_file:
    text = a_file.read()

print(text)

count = 0

for s in signs:
    count += len(signs)
    signs.append(text.strip())
    
    
    # for line in a_file:
    #     signs = a_file.read()
        
    # for line in a_file:
        # signs.append(line.strip())

print(count)

# count = 0

# for line in signs:
#     print(len(line))
#     count += len(line)

# print(count)

signs = {'a': count, 'b': text},

with open('hw01_output.json', mode='w', encoding='utf-8') as file:
    json.dump(signs, file)

     
     


