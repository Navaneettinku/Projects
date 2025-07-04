
import pandas as pd

# Load dataset
file_path = "D:/ML MODEL/preprocessed_songs.csv"
df = pd.read_csv(file_path)

# Display dataset structure
print(df.head())
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Select numerical features
features = ['danceability', 'energy', 'valence']

# Scale the features (important for similarity calculations)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])

# Compute cosine similarity
similarity_matrix = cosine_similarity(df_scaled)

# Convert to DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=df['track_name'], columns=df['track_name'])

# Display similarity matrix
print(similarity_df.head())



def recommend_songs(song_name, num_recommendations=5):
    if song_name not in similarity_df.index:
        print(f"❌ Song '{song_name}' not found in the dataset.")
        return []
    
    # Get similarity scores for the song
    similar_songs = similarity_df[song_name].sort_values(ascending=False)[1:num_recommendations+1]
    
    print(f"\n🎵 Songs similar to '{song_name}':\n")
    for i, (track, score) in enumerate(similar_songs.items(), start=1):
        artist = df[df['track_name'] == track]['artists'].values[0]
        print(f"{i}. {track} by {artist} (Similarity Score: {score:.2f})")
    
    return similar_songs.index.tolist()

# Example usage:
recommend_songs("Hold On")
