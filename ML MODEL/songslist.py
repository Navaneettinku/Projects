import pandas as pd

df = pd.read_csv("C:/ML MODEL/preprocessed_songs.csv")

# Display first 10 songs
print("\n🎵 First 10 Songs in the Dataset:\n")
print(df[['track_name', 'artists', 'mood']].head(10))

print(f"\n🎼 Total songs in the dataset: {len(df)}")
