import pandas as pd

# Load dataset
file_path = r"D:\ML MODEL\preprocessed_songs.csv"
df = pd.read_csv(file_path)

# Print available columns
print("Columns in dataset:", df.columns)

# Selecting the correct columns (Replacing 'artist_name' with 'artists')
df = df[['track_name', 'artists', 'danceability', 'energy', 'valence']]

# Display first few rows to verify
print(df.head())
