import pandas as pd
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
df = pd.read_csv("/home/ubuntu/Desktop/projects/anime_recommendation_system/anime.csv")

df = df.dropna(subset = ['genre'])
df['type'] = df['type'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mean())
df = df.drop_duplicates(subset = ['name'])
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove punctuation/numbers
    return text
df['combined_tags'] = df['name'].fillna('') + ' ' + df['genre'].fillna('') + ' ' + df['type'].fillna('')
df['combined_tags'] = df['combined_tags'].apply(clean_text)
vectorizer = TfidfVectorizer(stop_words = "english",min_df = 2,max_df = 0.8)
tfid_matrix = vectorizer.fit_transform(df['combined_tags'])

def recommend_anime(user_input,top_n = 5):
    input_vec = vectorizer.transform([user_input.lower()])
    if input_vec.nnz == 0: # .nnz = number of non-zero elements in sparse matrix
        print("❌ No recognizable keywords found in input. Try using tags like 'action', 'romance', 'sci-fi', etc.")
        return pd.DataFrame()  # or return None

    sim_scores = cosine_similarity(input_vec,tfid_matrix).flatten()
    valid_indices = np.where(sim_scores >=0.1)[0]
    if len(valid_indices)==0:
        print("No strong matches found, try different tags")
        return pd.DataFrame()
    top_indices = valid_indices[np.argsort(sim_scores[valid_indices])[-top_n:][::-1]]
    results = df.iloc[top_indices][['name', 'genre', 'type', 'rating']].copy()
    # results['similarity'] = sim_scores[top_indices]
    return results



    