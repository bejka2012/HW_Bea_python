import json

lines = []
movies = []

with open('netflix_titles.tsv', encoding='utf-8') as a_file:
    lines = a_file.readlines()[1:]
    
for line in lines:
    columns = line.split('\t')


movie = {
        "title": columns[2],
        "directors": columns[15].split(', '),
        "cast": columns[16].split(', '),
        "genres": columns[8].split(','),
        "decade": columns[5]
    }
movies.append(movie)



with open('hw02_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(movies, output_file, ensure_ascii=False, indent=4)
