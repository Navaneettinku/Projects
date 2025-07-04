import pandas as pd

# Load the preprocessed dataset
file_path = "C:/ML MODEL/preprocessed_songs.csv"
df = pd.read_csv(file_path)

# Display the first few rows
print(df.head())

# Get basic info about the dataset
print(df.info())

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())




import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))
sns.countplot(x=df['mood'], order=df['mood'].value_counts().index, palette='viridis')
plt.title("Mood Distribution in Songs Dataset")
plt.xticks(rotation=45)
plt.show()




features = ['danceability', 'energy', 'valence']

plt.figure(figsize=(12,4))
for i, feature in enumerate(features, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[feature], bins=30, kde=True, color='blue')
    plt.title(f'{feature.capitalize()} Distribution')

plt.tight_layout()
plt.show()




sns.pairplot(df[['danceability', 'energy', 'valence', 'mood']], hue='mood', palette='coolwarm')
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(df[['danceability', 'energy', 'valence']].corr(), annot=True, cmap='coolwarm', linewidths=1)
plt.title("Feature Correlation Heatmap")
plt.show()



mood_means = df.groupby('mood')[['danceability', 'energy', 'valence']].mean()

plt.figure(figsize=(12,6))
mood_means.plot(kind='bar', colormap='viridis')
plt.title("Average Feature Values for Each Mood")
plt.ylabel("Mean Value")
plt.xticks(rotation=45)
plt.show()

