import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_billboard_dataset.csv")

# Objective 2: Longest staying unique songs
longest_songs = df.groupby('song')['weeks-on-board'].max().sort_values(ascending=False).head(10)

print("\nTop 10 Longest Staying Songs:")
print(longest_songs)

# Plot graph
plt.figure(figsize=(12,6))

longest_songs.plot(kind='bar', color='skyblue')

plt.title("Top 10 Longest Staying Songs")
plt.xlabel("Song")
plt.ylabel("Weeks on Billboard")

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()