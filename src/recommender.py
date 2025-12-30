import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def recommend_movies(
    user_vector,
    genre_df,
    liked_ids=None,
    disliked_ids=None,
    top_n=5,
    required_genres=None
):
    

    if liked_ids is None:
        liked_ids = []
    if disliked_ids is None:
        disliked_ids = []
    if required_genres is None:
        required_genres = []

    # Compute similarity
    similarity_scores = cosine_similarity(
        user_vector.reshape(1, -1),
        genre_df.values
    )[0]

    scores_df = pd.DataFrame({
        "movieId": genre_df.index,
        "score": similarity_scores
    })

    # Remove already seen movies
    seen_ids = set(liked_ids) | set(disliked_ids)
    scores_df = scores_df[~scores_df["movieId"].isin(seen_ids)]

    # HARD FILTER: required genres
    for genre in required_genres:
        if genre in genre_df.columns:
            mask = genre_df.loc[
                scores_df["movieId"], genre
            ].values > 0

            scores_df = scores_df[mask]

    # Sort
    scores_df = scores_df.sort_values("score", ascending=False)

    return scores_df.head(top_n)

