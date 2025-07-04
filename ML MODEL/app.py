import streamlit as st
import pandas as pd
import re
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# --- Load & preprocess data ---
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath, low_memory=False)
    # Convert feature cols to numeric
    features = ['danceability', 'energy', 'valence']
    for col in features:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna(subset=features).reset_index(drop=True)
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df[features])
    return df, df_scaled

# Normalize song names
def normalize_text(text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text).lower().strip()

# Recommend songs
def recommend_songs(song_name, df_scaled, df, num_recommendations=5):
    normalized_input = normalize_text(song_name)
    df['normalized_name'] = df['track_name'].apply(normalize_text)
    if normalized_input not in df['normalized_name'].values:
        return None
    song_idx = df[df['normalized_name'] == normalized_input].index[0]
    target_vector = df_scaled[song_idx].reshape(1, -1)
    sim_scores = cosine_similarity(target_vector, df_scaled).flatten()
    top_indices = sim_scores.argsort()[::-1][1:num_recommendations+1]
    return df.iloc[top_indices][['track_name', 'artists', 'mood']]

# --- Streamlit UI ---
st.title("🎵 Song Recommendation App")

# Load data
df, df_scaled = load_data("C:/ML MODEL/preprocessed_songs.csv")

# User input
song_name = st.text_input("Enter a song name:")

if song_name:
    recommended = recommend_songs(song_name, df_scaled, df)
    if recommended is not None:
        st.write("Here are your recommendations:")
        st.dataframe(recommended)
    else:
        st.warning("❌ Song not found. Please check the spelling!")

