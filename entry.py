# importing stuffs
import movie
import fresh_tomatoes

# declaring movies
sideways = movie.Movie(
    "Sideways",
    "Two men reaching middle age with not much to show but disappointment, embark on a week long road trip through California's wine country, just as one is about to take a trip down the aisle.",
    "http://ia.media-imdb.com/images/M/MV5BMTU0Mjg3MzkxOV5BMl5BanBnXkFtZTYwNDU1OTY3._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=YS9ocP6FNvM",
    "2004"
)

star_wars = movie.Movie(
    "Star Wars: Episode V - The Empire Strikes Back",
    "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
    "http://ia.media-imdb.com/images/M/MV5BMjE2MzQwMTgxN15BMl5BanBnXkFtZTcwMDQzNjk2OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
    "1980"
)

american_history_x = movie.Movie(
    "American History X",
    "A former neo-nazi skinhead tries to prevent his younger brother from going down the same wrong path that he did.",
    "http://ia.media-imdb.com/images/M/MV5BMjMzNDUwNTIyMF5BMl5BanBnXkFtZTcwNjMwNDg3OA@@._V1_SY317_CR17,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=XfQYHqsiN5g",
    "1998"
)

# adding individual movies to array
movies = [sideways, star_wars, american_history_x]

# calling fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
