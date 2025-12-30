def ratings_to_preferences(
    ratings_df,
    user_id,
    like_threshold=4.0,
    dislike_threshold=2.0
):
    
    # Convert user ratings into liked and disliked movie IDs.
    

    user_ratings = ratings_df[ratings_df["userId"] == user_id]

    liked_ids = user_ratings[
        user_ratings["rating"] >= like_threshold
    ]["movieId"].tolist()

    disliked_ids = user_ratings[
        user_ratings["rating"] <= dislike_threshold
    ]["movieId"].tolist()

    return liked_ids, disliked_ids
