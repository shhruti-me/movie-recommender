import pandas as pd
import os


def save_preferences(user_id, liked_ids, disliked_ids, path="data/user_preferences.csv"):
    rows = []

    for mid in liked_ids:
        rows.append({"userId": user_id, "movieId": mid, "preference": "like"})

    for mid in disliked_ids:
        rows.append({"userId": user_id, "movieId": mid, "preference": "dislike"})

    if not rows:
        return

    df = pd.DataFrame(rows)

    # If file doesn't exist or is empty, write header
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0

    df.to_csv(
        path,
        mode="a",
        header=write_header,
        index=False
    )


def load_preferences(user_id, path="data/user_preferences.csv"):
    import os
    import pandas as pd

    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return [], []

    df = pd.read_csv(path)

    # Defensive check for required columns
    required_cols = {"userId", "movieId", "preference"}
    if not required_cols.issubset(df.columns):
        raise ValueError(
            f"user_preferences.csv must contain columns {required_cols}, "
            f"but found {set(df.columns)}"
        )

    user_df = df[df["userId"] == user_id]

    liked_ids = user_df[user_df["preference"] == "like"]["movieId"].tolist()
    disliked_ids = user_df[user_df["preference"] == "dislike"]["movieId"].tolist()

    return liked_ids, disliked_ids

