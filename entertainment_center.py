import media
import fresh_tomatoes

# media object for movie Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org"\
                        "/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# media object for movie avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org"\
                     "/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

# media object for movie school of rock
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org"\
                             "/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# media object for movie ratatouille
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org"\
                          "/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# media object for movie midnight in paris
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "http://upload.wikimedia.org"\
                                "/wikipedia/en/9/9f"\
                                "/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

# media object for movie hunger games
hunger_games = media.Movie("Hunger Games",
                           "Storyline",
                           "http://upload.wikimedia.org"\
                           "/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

# list of all movie objects
movies = [toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

# generates movie trailer websites with the list of movies
fresh_tomatoes.open_movies_page(movies)
