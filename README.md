**Explainable Movie Recommendation System**

This project implements an explainable, content-based movie recommendation system that learns a user’s taste from explicit likes and dislikes, enforces core preference constraints, and explains recommendations by referencing movies the user already likes.

Unlike basic genre-based recommenders that often collapse to generic results (e.g., only “Drama”), this system captures nuanced preferences such as romantic dramas or emotionally intense films and produces human-readable explanations for every recommendation.

**Features**

- Explicit user preference input (likes and dislikes)
- Persistent storage of user preferences
- TF-IDF weighted genre representation
- Genre-pair features (e.g., Drama_Romance) to capture nuanced taste
- User preference modeling with weighted and overlap-aware signals 
- Constraint-based filtering using automatically detected core genres  
- Cosine similarity–based ranking 
- Explainable recommendations referencing similar liked movies

**How It Works**

Movie Representation
    Movies are represented using TF-IDF–weighted genre features, including individual genres and genre pairs.
    
User Preference Modeling
    A user preference vector is built from liked and disliked movies. Repeated genre patterns across liked movies are boosted, while disliked genres are penalized.
    
Core Preference Detection
    Genres and genre-pairs that appear consistently in the user’s liked movies are identified as core preferences.
    
Candidate Filtering
    Only movies that satisfy these core preferences are considered for recommendation.
    
Ranking
    Cosine similarity is used to rank candidate movies against the user preference vector.
    
Explanation
    Each recommendation is explained by identifying the most similar liked movies and describing the shared genre patterns.

**Example Explanation**

Recommended because you liked “Sita Ramam (2022)” and “Dear Comrade (2019)”, which share Drama and Romance elements with this movie.

**Project Structure**

    <img width="321" height="459" alt="image" src="https://github.com/user-attachments/assets/504bc12c-b770-419d-9cc2-a8510e84ff78" />


**Dataset**

This project uses the MovieLens dataset provided by GroupLens.  
Due to licensing and size constraints, the dataset is not included in this repository.

**To run the project:**

- Download the MovieLens dataset from https://grouplens.org/datasets/movielens/   
- Extract movies.csv (and optionally ratings.csv)  
- Place the files inside the data/ directory

**Requirements**

- Python 3.9+
- pandas
- numpy
- scikit-learn
- Install dependencies with:
- pip install -r requirements.txt

**How to Run**
python main.py


**You will be prompted to enter:**
    Movies you like
    Movies you dislike
    The system will then output recommended movies along with explanations.

**This project focuses on:**
- Explicit negative feedback
- Avoiding genre collapse
- Constraint-based recommendation behavior
- Explainability and user trust

**Future Improvements**
- Soft constraints for greater recommendation diversity
- Rating-based weighting of user preferences
- Tag-based or embedding-based semantic features
- Web interface using Flask or FastAPI



