
# Load required library
library(ggplot2)

# Read the dataset
df <- read.csv("Netflix_shows_movies.csv", stringsAsFactors = FALSE)

# Create Ratings Distribution Plot
ggplot(df, aes(x = rating)) +
  geom_bar(fill = "steelblue") +
  theme_minimal() +
  labs(title = "Distribution of Ratings on Netflix", x = "Rating", y = "Count")
