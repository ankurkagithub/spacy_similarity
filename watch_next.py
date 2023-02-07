'''
Details: 
Using spacy NLP model for Text similarity, this program checks 2 movie descriptions
for similariy and returns most similar movie.
The movies data containing names and description is loaded from a text file.
Spacy's language model called "en_core_web_md" is used to checked similarity
between text and create a new suggestion based on highest similarity ratings.
'''



def similar_movie(description):
    # importing spacy
    import spacy

    #loading NLP model for similiary check, different from 'en_core_web_sm'
    nlp = spacy.load('en_core_web_md')

    movie_similarity_probability = []
    # Reading data from movies.txt
    with open('movies.txt', 'r') as file:
        movies = file.readlines()
        doc = nlp(description)
        for movie in movies:
            sim_value = doc.similarity(nlp(movie))
            movie_similarity_probability.append(sim_value)
        similar_movie_index = movie_similarity_probability.index(max(movie_similarity_probability))
        return movies[similar_movie_index]


def main():

    # Name and details of the movie which user recently watched
    watched_movie_name = "Planet Hulk"
    watched_movie_description = """Will he save their world or destroy it? When the
    Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle
    and launch him into space to a planet where the Hulk can live in peace.
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery
    and trained as a gladiator."""

    #formatting name prior to function call
    movie = f"{watched_movie_name}: {watched_movie_description}"

    #Calling function
    new_movie_suggestion = similar_movie(movie)
    print(new_movie_suggestion)

if __name__ == "__main__":
    main()
