favorite_movies = ["FastNFurious", "Spiderman1", "HarryPotter"]
print(f'The list favorite_movies includes my top {len(favorite_movies)} favorite movies')
print(favorite_movies)

print()

print(sorted(favorite_movies))
print(favorite_movies)
# I noticed that the sorted() function ordered my list of favorite movies in alphabetical order.

print()

favorite_movies.sort()
print(favorite_movies)
# I noticed that it sorted favorite_movies alphabetically.

print()

favorite_movies.append('Interstellar')
print(f'Here is my top {len(favorite_movies)} list of favorite_movies:')
print(favorite_movies)