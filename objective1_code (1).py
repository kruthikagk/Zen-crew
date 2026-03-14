import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
chart = pd.read_csv("chart_positions.csv")
artist = pd.read_csv("artist_info.csv")

# Clean artist names safely
chart['artist'] = chart['artist'].astype(str).str.strip().str.lower()
artist['artist'] = artist['artist'].astype(str).str.strip().str.lower()

# Clean song names safely
chart['song'] = chart['song'].astype(str).str.strip().str.lower()

# Remove duplicate artist rows
artist = artist.drop_duplicates(subset='artist')

# Convert date column safely
chart['date'] = pd.to_datetime(chart['date'], errors='coerce')

# Merge datasets
df = pd.merge(chart, artist, on='artist', how='left')

# Remove true duplicate weekly entries only
df = df.drop_duplicates(subset=['song', 'artist', 'date'])

# Fill missing values
df['weeks-on-board'] = df['weeks-on-board'].fillna(0)
df['peak-rank'] = df['peak-rank'].fillna(0)
df['last-week'] = df['last-week'].fillna(0)

# Create year and decade columns
df['year'] = df['date'].dt.year
df['decade'] = (df['year'] // 10) * 10

# Save cleaned merged dataset
df.to_csv("cleaned_billboard_dataset.csv", index=False)

# Show first rows
print("\nCleaned Merged Dataset:")
print(df.head())

# Objective 1: Top 10 artists by Billboard appearances
top_artists = df['artist'].value_counts().head(10)

print("\nTop 10 Artists by Billboard Entries:")
print(top_artists)

# Plot graph
plt.figure(figsize=(12,6))

top_artists.plot(kind='bar', color='skyblue')

plt.title("Top 10 Artists by Billboard Entries")
plt.xlabel("Artist")
plt.ylabel("Number of Entries")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()