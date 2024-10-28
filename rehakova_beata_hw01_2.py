
# Ahoj Jirko,
# posilam Ti druhy pokus.


import json

with open("alice.txt", encoding="utf-8") as a_file:
    text = a_file.read()

text = text.lower()

print(text)

signs = {}

for s in text:
    if s != ' ' and s != '\n':
        if s in signs:
            signs[s] += 1

        else:
            signs[s] = 1


print(f"{signs}, '\n'")


with open('hw01_output.json', mode='w', encoding='utf-8') as file:
    json.dump(signs, file, ensure_ascii=False, )
    

    #  , sort_keys= True, separators=(',', ': '), indent= 4
     


