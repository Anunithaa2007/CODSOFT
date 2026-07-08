import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("movies.csv")
print(movies.head())

# Convert movie descriptions into numerical vectors
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(movies["description"])

# Calculate similarity between all movies
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
def recommend(movie_name):
    # Check if the movie exists
    if movie_name not in movies["title"].values:
        print("Movie not found!")
        return

    # Get the movie index
    index = movies[movies["title"] == movie_name].index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[index]))

    # Sort movies by similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    # Show top 5 recommendations
    for i in scores[1:6]:
        print(movies.iloc[i[0]]["title"])

movie = input("Enter a movie name: ")

recommend(movie)