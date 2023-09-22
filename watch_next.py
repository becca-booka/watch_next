# LEVEL 3, TASK 12: SEMANTIC SIMILARITY
# COMPULSORY TASK 2

# REFERENCES:
# had a lot of help from my mom
# I didn't know where to start and got confused

# create a program that suggests a movie to the user based 
# on the description of the movie "Planet Hulk"
# by compairing the movie descriptions of the movies in the provided txt file
# to that of "Planet Hulk"
# and returning the title of the movie with the most similar description

# import spacy
import spacy

# FUNCTION...........................................................

# create function
def next_movie(just_watched):
    # set up variables
    nlp = spacy.load('en_core_web_md')
    favourite = nlp(just_watched)
    movie_list = []
    movie_level = 0
    similarity_level = 0

    # read txt document
    with open('movies.txt', 'r') as m:
        lines = m.readlines()

        # using for loop to go through each line
        # split the movie titles from description at the ":"
        # run descriptions through language model
        # compare movie descriptions to get simialrity level
        # return movie title with the most similar description

        for l in lines:
            movie_list = l.split(":")
            movie_options = nlp(movie_list[1])
            movie_level = movie_options.similarity(favourite)
            # print the movie title, description and its similarity level
            print(f'''Movie: {movie_list[0]} -- Level:{movie_level}   
Description: {movie_list[1]}''')
            
            # compare the different movies similarity levels
            # to find the one that ranked the highest
            # and then return the title of that movie

            if movie_level > similarity_level:
                next_movie = movie_list[0]
                similarity_level = movie_level

    return next_movie 

#.............................................................................

# description of the movie we just watched ("Planet Hulk")
just_watched = '''Will he save their world or destroy it?
    When the Hulk becomes too dangerous for the Earth, the
    Illuminati trick Hulk into a shuttle and launch him
    into space to a planet where the Hulk can live in peace.
    Unfortunately, Hulk lands on the planet Sakaar where he
    is sold into slavery and trained as a gladiator.'''

# print just_watched movie title and description
print(f'''Just watched: "Planet Hulk"
Description: {just_watched}
''')

# call on fucntion to suggest a new movie
new_movie = next_movie(just_watched)
print(f"Next movie: {new_movie}")