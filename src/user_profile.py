import numpy as np


def build_user_profile(liked_ids, disliked_ids, genre_df):
    
    # Keep only valid movie IDs
    liked_ids = [mid for mid in liked_ids if mid in genre_df.index]
    disliked_ids = [mid for mid in disliked_ids if mid in genre_df.index]

    if not liked_ids and not disliked_ids:
        raise ValueError("User must like or dislike at least one movie.")

    # LIKED MOVIES 
    if liked_ids:
        liked_vectors = genre_df.loc[liked_ids]

        # Weight movies inversely by number of genres
        genre_counts = (liked_vectors > 0).sum(axis=1)
        weights = 1 / genre_counts

        weighted_liked = liked_vectors.mul(weights, axis=0)

        liked_vector = weighted_liked.mean(axis=0).values

        # Boost genres that appear in multiple liked movies
        overlap_boost = (liked_vectors > 0).sum(axis=0).values
        liked_vector = liked_vector * overlap_boost
    else:
        liked_vector = np.zeros(genre_df.shape[1])

    #  DISLIKED MOVIES 
    if disliked_ids:
        disliked_vectors = genre_df.loc[disliked_ids]
        disliked_vector = disliked_vectors.mean(axis=0).values
    else:
        disliked_vector = np.zeros(genre_df.shape[1])

    #  FINAL USER VECTOR 
    user_vector = liked_vector - disliked_vector

    # Normalize for cosine similarity
    norm = np.linalg.norm(user_vector)
    if norm != 0:
        user_vector = user_vector / norm

    return user_vector
