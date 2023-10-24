def movie_organizer(*args):
    movies = {}
    for movie in args:
        if movie[1] not in movies:
            movies[movie[1]] = [movie[0]]
            continue

        movies[movie[1]].append(movie[0])

    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))
    res = ''
    for g, m in sorted_movies:
        res += f'{g} - {len(m)}\n'
        n = sorted(m, reverse=False)
        for i in n:
            res += f'* {i}\n'

    return res


print(movie_organizer(("Avatar: The Way of Water", "Action"),
                      ("House Of Gucci", "Drama"),
                      ("Top Gun", "Action"),
                      ("Ted", "Comedy"),
                      ("Duck Soup", "Comedy"),
                      ("The Dark Knight", "Action"),
                      ("A Star Is Born", "Musicals"),
                      ("The Warrior", "Action"),
                      ("Like A Boss", "Comedy"),
                      ("The Green Mile", "Drama"),
                      ("21 Jump Street", "Comedy")))
