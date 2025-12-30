import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from itertools import combinations


def expand_genres(genres):
    # Create genre + genre-pair features.
    base = genres.split("|")
    pairs = ["_".join(pair) for pair in combinations(base, 2)]
    return " ".join(base + pairs)


def build_genre_matrix(movies_df):
    #Build TF-IDF genre + genre-pair feature matrix.

    expanded_genres = movies_df["genres"].apply(expand_genres)

    tfidf = TfidfVectorizer(
        token_pattern=r"[^ ]+",
        lowercase=False,
        norm="l2"
    )

    genre_tfidf = tfidf.fit_transform(expanded_genres)

    genre_df = pd.DataFrame(
        genre_tfidf.toarray(),
        columns=tfidf.get_feature_names_out(),
        index=movies_df["movieId"]
    )

    return genre_df
