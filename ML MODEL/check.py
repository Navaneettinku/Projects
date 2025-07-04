import pandas as pd

# Load dataset
file_path = r"C:\ML MODEL\preprocessed_songs.csv"
df = pd.read_csv(file_path)

# Print available columns
print("Columns in dataset:", df.columns)

# Selecting the correct columns (Replacing 'artist_name' with 'artists')
df = df[['track_name', 'artists', 'danceability', 'energy', 'valence']]

# Display first few rows to verify
print(df.head())


import pandas as pd

# Load dataset
file_path = "C:\\ML MODEL\\preprocessed_songs.csv"
df = pd.read_csv(file_path)

# Function to classify mood
def classify_mood(row):
    if row['valence'] > 0.6 and row['energy'] > 0.6:
        return 'Happy'
    elif row['valence'] < 0.4 and row['energy'] < 0.4:
        return 'Sad'
    elif row['energy'] > 0.7:
        return 'Energetic'
    else:
        return 'Calm'

# Apply function to create 'mood' column
df['mood'] = df.apply(classify_mood, axis=1)

# Save updated dataset
df.to_csv("C:\\ML MODEL\\songs_with_mood.csv", index=False)

# Check results
print(df[['track_name', 'artists', 'mood']].head())

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.countplot(x=df['mood'], palette='viridis')
plt.title("Mood Distribution in Songs Dataset")
plt.show()

