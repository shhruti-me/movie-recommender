def titles_to_ids(titles, movies_df):
    ids = []
    not_found = []

    for title in titles:
        match = movies_df[
            movies_df["title"].str.lower().str.contains(title.lower())
        ]

        if not match.empty:
            ids.append(int(match.iloc[0]["movieId"]))
        else:
            not_found.append(title)

    return ids, not_found
