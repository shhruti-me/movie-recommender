def get_user_input():
    """
    Collect liked and disliked movie titles from user.
    """
    print("Enter movies you LIKE (comma-separated):")
    liked_input = input("> ")

    print("Enter movies you DISLIKE (comma-separated):")
    disliked_input = input("> ")

    liked_titles = [m.strip() for m in liked_input.split(",") if m.strip()]
    disliked_titles = [m.strip() for m in disliked_input.split(",") if m.strip()]

    return liked_titles, disliked_titles
