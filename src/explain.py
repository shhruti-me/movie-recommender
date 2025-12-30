import numpy as np


def explain_recommendation(
    movie_id,
    movies_df,
    genre_df,
    user_vector,
    liked_ids,
    top_k=2
):

    # Get recommended movie info
    rec_movie = movies_df[movies_df["movieId"] == movie_id].iloc[0]
    rec_title = rec_movie["title"]
    rec_genres = set(rec_movie["genre_list"])

    # Compare with liked movies
    similarities = []

    for liked_id in liked_ids:
        liked_movie = movies_df[movies_df["movieId"] == liked_id].iloc[0]
        liked_vector = genre_df.loc[liked_id].values
        rec_vector = genre_df.loc[movie_id].values

        sim = np.dot(liked_vector, rec_vector)
        similarities.append((liked_movie["title"], liked_movie["genre_list"], sim))

    # Pick most similar liked movies
    similarities.sort(key=lambda x: x[2], reverse=True)
    top_similar = similarities[:top_k]

    # Extract shared genres
    shared_genres = set()
    for _, genres, _ in top_similar:
        shared_genres |= (set(genres) & rec_genres)

    # Build explanation text
    if top_similar:
        movie_refs = ", ".join([f"“{m[0]}”" for m in top_similar])
        if shared_genres:
            genre_text = ", ".join(shared_genres)
            explanation = (
                f"Recommended because you liked {movie_refs}, "
                f"which share {genre_text} elements with this movie."
            )
        else:
            explanation = (
                f"Recommended because it is similar in style to movies you liked, "
                f"such as {movie_refs}."
            )
    else:
        explanation = "Recommended based on your overall preferences."

    return rec_title, explanation
