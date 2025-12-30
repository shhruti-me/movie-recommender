import pandas as pd


def load_movies(path="data/movies.csv"):
    
    # Load CSV
    movies = pd.read_csv(path)

    # Basic validation
    required_cols = {"movieId", "title", "genres"}
    if not required_cols.issubset(movies.columns):
        raise ValueError(
            f"Dataset must contain columns: {required_cols}"
        )

    # Handle missing / empty genres
    movies["genres"] = (
        movies["genres"]
        .fillna("Unknown")
        .replace("(no genres listed)", "Unknown")
    )

    # Split genres into list
    movies["genre_list"] = movies["genres"].apply(lambda x: x.split("|"))

    # Ensure movieId is integer (important later)
    movies["movieId"] = movies["movieId"].astype(int)

    return movies
