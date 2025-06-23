
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Netflix_shows_movies.csv")

# Data Cleaning
df.fillna({'director': 'Unknown', 'cast': 'Unknown', 'country': 'Unknown', 'rating': 'Not Rated', 'date_added': 'Unknown'}, inplace=True)

# Genre Visualization
plt.figure(figsize=(10,6))
genre_counts = df['listed_in'].str.split(', ').explode().value_counts().head(10)
sns.barplot(y=genre_counts.index, x=genre_counts.values)
plt.title('Top 10 Most Watched Genres on Netflix')
plt.xlabel('Number of Shows')
plt.ylabel('Genres')
plt.tight_layout()
plt.savefig("top_genres.png")

# Rating Distribution
plt.figure(figsize=(10,6))
sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index)
plt.title('Distribution of Ratings')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.tight_layout()
plt.savefig("ratings_distribution.png")
