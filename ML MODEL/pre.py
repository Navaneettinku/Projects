import pandas as pd

# Load dataset
file_path = "C:/ML MODEL/preprocessed_songs.csv"  # Change this to your actual dataset path
df = pd.read_csv(file_path)

# Display first few rows
print("🔹 First 5 rows of dataset:")
print(df.head())

# Display column names
print("\n🔹 Columns in dataset:")
print(df.columns)


# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df = df.dropna()  # If you want to remove rows with missing values
# df.fillna(df.mean(), inplace=True)  # Alternative: Fill missing values with mean

print("\n✅ Data cleaned. Shape of dataset:", df.shape)



from sklearn.preprocessing import MinMaxScaler

# List of numerical columns to normalize
num_cols = ['danceability', 'energy', 'valence']

# Apply MinMax Scaling
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\n✅ Numerical features normalized.")

