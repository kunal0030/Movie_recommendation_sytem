# 🎬 Movie Recommendation System (Streamlit App)

A **content-based Movie Recommendation System** built with **Python, Streamlit, and Machine Learning**.  
It suggests movies to users based on similarity scores calculated from movie features such as genres, keywords, cast, and crew.

---

## 📌 Features

- Recommend movies similar to a given movie title  
- Simple and interactive **Streamlit web interface**  
- Pre-trained similarity model for fast recommendations  
- Fetches **movie posters** using the TMDB API  
- Runs locally or can be deployed on Streamlit Cloud

---

##📊 How It Works
#Data Preprocessing
1.Reads a dataset of movies
2.Combines features like overview, genres, keywords, cast, and crew

#Feature Extraction
1.Uses TF-IDF Vectorization or Count Vectorization

#Similarity Calculation
1.Uses cosine similarity to find the most similar movies

#Streamlit UI
1.User selects a movie from a dropdown

