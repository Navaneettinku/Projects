import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def preprocess_features(df):
    features = ['danceability', 'energy', 'valence']
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df[features])
    return df_scaled

def build_similarity_model(df_scaled):
    nn = NearestNeighbors(metric='cosine', algorithm='brute')
    nn.fit(df_scaled)
    return nn  # Return trained NearestNeighbors model

def recommend_songs(song_name, df, nn_model, df_scaled, num_recommendations=5):
    if song_name not in df['track_name'].values:
        return "❌ Song not found in dataset. Please try another song."
    
    song_idx = df[df['track_name'] == song_name].index[0]
    distances, indices = nn_model.kneighbors([df_scaled[song_idx]], n_neighbors=num_recommendations+1)
    
    recommended_songs = df.iloc[indices[0][1:]][['track_name', 'artists', 'mood']]
    return recommended_songs

# Load and preprocess data
df = load_data("C:/ML MODEL/preprocessed_songs.csv")
df_scaled = preprocess_features(df)
nn_model = build_similarity_model(df_scaled)

# Take user input
while True:
    song_to_recommend = input("\n🎵 Enter a song name (or type 'exit' to quit): ").strip()
    if song_to_recommend.lower() == 'exit':
        print("👋 Exiting the recommendation system. Goodbye!")
        break
    
    recommendations = recommend_songs(song_to_recommend, df, nn_model, df_scaled)
    
    if isinstance(recommendations, str):  # If song is not found
        print(recommendations)
    else:
        print("\n🎶 Recommended Songs:\n", recommendations.to_string(index=False))
