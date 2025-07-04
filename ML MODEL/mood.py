import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (Make sure the file exists at this path)
file_path = r"C:\ML MODEL\preprocessed_songs.csv"  # Change this to the actual path of your dataset

try:
    df = pd.read_csv(file_path)

    # Check if the 'mood' column exists
    if 'mood' not in df.columns:
        print("Error: 'mood' column not found in dataset.")
    else:
        # Handle missing values
        df['mood'] = df['mood'].fillna('Unknown')

        # Plot mood distribution
        plt.figure(figsize=(10, 5))
        sns.countplot(x=df['mood'], order=df['mood'].value_counts().index, palette='viridis')
        plt.title("Mood Distribution in Songs Dataset")
        plt.xticks(rotation=45)
        plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Check the path and try again.")

except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
