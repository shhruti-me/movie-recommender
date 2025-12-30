import pandas as pd

from src.data_loader import load_movies
from src.feature_engineering import build_genre_matrix
from src.user_input import get_user_input
from src.movie_lookup import titles_to_ids
from src.preferences_store import save_preferences, load_preferences
from src.user_profile import build_user_profile
from src.recommender import recommend_movies
from src.explain import explain_recommendation


def main():
    #  LOAD DATA 
    movies = load_movies()
    genre_df = build_genre_matrix(movies)

    USER_ID = 1

    #  USER INPUT 
    liked_titles, disliked_titles = get_user_input()

    liked_ids, not_found_likes = titles_to_ids(liked_titles, movies)
    disliked_ids, not_found_dislikes = titles_to_ids(disliked_titles, movies)

    if not_found_likes:
        print(" Could not find (likes):", not_found_likes)
    if not_found_dislikes:
        print(" Could not find (dislikes):", not_found_dislikes)

    # Save preferences
    save_preferences(USER_ID, liked_ids, disliked_ids)

    # Load preferences (persistent)
    liked_ids, disliked_ids = load_preferences(USER_ID)

    if not liked_ids and not disliked_ids:
        print("No preferences found.")
        return

    #  USER PROFILE 
    user_vector = build_user_profile(liked_ids, disliked_ids, genre_df)

    #  CORE GENRE DETECTION 
    liked_vectors = genre_df.loc[liked_ids]
    genre_counts = (liked_vectors > 0).sum(axis=0)

    # Genres appearing in at least 2 liked movies = CORE taste
    required_genres = genre_counts[genre_counts >= 2].index.tolist()

    print("\n Core preference genres detected:", required_genres)

    #  RECOMMEND MOVIES
    recs = recommend_movies(
        user_vector,
        genre_df,
        liked_ids=liked_ids,
        disliked_ids=disliked_ids,
        top_n=5,
        required_genres=required_genres
    )

    print("\n Recommended movies:\n")

    for _, row in recs.iterrows():
        title, reason = explain_recommendation(
            row["movieId"],
            movies,
            genre_df,
            user_vector, 
            liked_ids 
        )

        movie_genres = movies[
            movies["movieId"] == row["movieId"]
        ]["genres"].values[0]

        print(f"{title} ({movie_genres})")
        print("→", reason, "\n")


if __name__ == "__main__":
    main()
