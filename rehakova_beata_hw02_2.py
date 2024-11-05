import json

lines = []
movies = []

with open('netflix_titles.tsv', encoding='utf-8') as a_file:
    lines = a_file.readlines()[1:]
    
for line in lines:
    columns = line.split('\t')

    if columns[15] == "":
        directors = []
    else:
        directors = columns[15].split(', ')
        
    if columns[16] == "":
        actors = []
    else:
        actors = columns[16].split(', ')

    movie = {
        "title": columns[2],
        "directors": directors,
        "cast": actors,
        "genres": columns[8].split(','),
        "decade": int(columns[5]) - int(columns[5]) % 10
    }
    movies.append(movie)



with open('hw02_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(movies, output_file, ensure_ascii=False, indent=4)



# Dekáda je vždy první rok desetiletí, např. rok 1987 patří do dekády 1980 a rok 2017 do dekády 2010.






    # print(title)
    # print(directors)

    # print(columns[1])
    # print(columns[2])


# title = columns[2]
# print(title)

# director = columns[15]
# print(director)

# movie = {
#     "title": title,
#     "directors": director
# }
# print(movie)

# # movies = [movie]
# # print(movies)

# movies = []
# movies.append(movie)

# print(movies)

# for key, value in lines():
#     print(title)


# 



# with open('hw02_output.json', mode='w', encoding='utf-8') as file:
#     json.dump(lines, file, ensure_ascii=False, )
    