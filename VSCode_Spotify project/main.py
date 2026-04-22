import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from kneed import KneeLocator
from sklearn.decomposition import PCA

import missing_values
import outlayers




# Read the csv file
df = pd.read_csv("/Users/ujjwalmanikyanath/Desktop/Data Science course/Module_3_Machine Learning/Project - Creating Cohorts of Songs/rolling_stones_spotify.csv")

# Print the head
print(df.head())

# Information about the data set
df.info()

#list of the columns
print(df.columns)

# Drop column
df = df.drop(columns= ['Unnamed: 0'])

#list of the columns after drop
print(df.columns)

# Idnetify the duplicates
print(df.duplicated())

# Drop the duplicates
print(df.drop_duplicates())

# Idintify the null values
print(df.isnull().sum())

# Print the missing values
print(missing_values.missing_values_table(df))

# Describe 
print(df.describe())

# Outlayers
column = 'acousticness'
outlayers.outlayer(df, column)

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the 'color' column
df['album_encoded'] = label_encoder.fit_transform(df['album'])

print(df)

### Perform Exploratory Data Analysis and Feature Engineering:

#############
# 1. Use appropriate visualizations to find out which two albums should be recommended to anyone based on the number of popular songs in an album.

# Step 1: Define the popularity threshold
POPULARITY_THRESHOLD = 75

# Step 2: Filter only popular songs
popular_songs = df[df['popularity'] >= POPULARITY_THRESHOLD]
print('popular_songs \n:', popular_songs.head())

# Step 3: Visualization 
plt.figure(figsize=(10, 6))
sns.barplot(data=popular_songs, x='album', y='popularity', palette='viridis', hue = 'album')
plt.title('Popularity level of the songs')
plt.xlabel('Album')
plt.ylabel('Popularity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 4: Recommend top 2 albums
top_albums = popular_songs.head(2)
print("\n 🎧 Recommend these two albums based on popular songs:\n", top_albums)

##########
# 2. Perform exploratory data analysis to dive deeper into different features of songs and identify the pattern.

# step -1: Distribution Plots of Key Features
features = ['popularity', 'danceability', 'energy', 'tempo', 'valence']

for feature in features:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[feature], kde=True, bins=20, color='skyblue')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

#step - 2: Correlation Heatmap
plt.figure(figsize=(10, 8))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Audio Features")
plt.tight_layout()
plt.show()


# step - 3: Pair Plot of Selected Features
sns.pairplot(df[['popularity', 'danceability', 'energy', 'valence', 'tempo']])
plt.suptitle('Pairwise Relationships Between Features', y=1.02)
plt.tight_layout()
plt.show()

# step- 4: Popularity by Album
plt.figure(figsize=(8, 5))
ax = sns.boxplot(data=df, x='album_encoded', y='popularity', palette='viridis', hue = 'album')
ax.legend(title='Decade', bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0.)
plt.title("Distribution of Popularity by Album")
plt.xticks(rotation=90)
plt.xticks(fontsize=7)
plt.tight_layout()
plt.show()

# step- 5: Top Songs with High Danceability or Energy
top_dance = df.sort_values(by='danceability', ascending=False).head(5)
top_energy = df.sort_values(by='energy', ascending=False).head(5)

print("Top 5 Danceable Songs:\n", top_dance[['album', 'danceability']])
print("\nTop 5 Energetic Songs:\n", top_energy[['album', 'energy']])

###############
# 3. Discover how a song's popularity relates to various factors and how this has changed over time.

# factor-1: Correlation Between Popularity and Features
# Correlation heatmap
plt.figure(figsize=(10, 7))
corr = df[['popularity', 'danceability', 'energy', 'valence', 'tempo', 'duration_ms']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation with Popularity")
plt.show()


# factor -2:  Trend of Popularity Over Time
# Group by year and average features
yearly = df.groupby('release_date')[['popularity', 'danceability', 'energy', 'valence']].mean().reset_index()

# Plot trend lines
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly, x='release_date', y='popularity', label='Popularity')
sns.lineplot(data=yearly, x='release_date', y='danceability', label='Danceability')
sns.lineplot(data=yearly, x='release_date', y='energy', label='Energy')
sns.lineplot(data=yearly, x='release_date', y='valence', label='Valence')
plt.title("Trends Over Time (1964–2022)")
plt.xlabel("Date")
plt.xticks(rotation=90)
plt.tight_layout()
plt.ylabel("Average Value")
plt.legend()
plt.grid(True)
plt.show()

# factor 3: Popularity Have Changed Over Time

# Convert to datetime if not already
df['release_date'] = pd.to_datetime(df['release_date'])

# Extract year
df['release_year'] = df['release_date'].dt.year

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='release_year', y='popularity', label='popularity')
plt.title("Change the Popularity Over Time")
plt.ylabel("Popularity Coefficient")
plt.grid(True)
plt.tight_layout()
plt.show()


# factor- 4: Popular vs Non-Popular Songs: Feature Comparison

df1 = df

# Categorize songs
df1['popularity'] = ['High' if p >= 70 else 'Low' for p in df1['popularity']]

# Boxplots of features
features = ['danceability', 'energy', 'valence', 'tempo']

for feature in features:
    plt.figure(figsize=(7, 4))
    sns.boxplot(x='popularity', y=feature, data=df1, palette='Set2')
    plt.title(f'{feature.capitalize()} by Popularity Level')
    plt.tight_layout()
    plt.show()

################
### Perform Cluster Analysis:

# Select numeric columns only (you can adjust this)
df_numeric = df.select_dtypes(include='number')

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_numeric)

# Method- 1: Initia calculation

inertia = []
K = range(1, 11)

for k in K:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(df_numeric)
    inertia.append(model.inertia_)

plt.figure(figsize=(8, 4))
sns.lineplot(x=K, y=inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
plt.title('Elbow Method For Optimal k')


# Find the Knee Locator to identify optimal point
kneedle = KneeLocator(K, inertia, curve="convex", direction="decreasing")
optimal_k = kneedle.knee

# Give the arrow mark to the optimal point 
plt.annotate("", xy=(optimal_k, inertia[2]), xytext=(4, 0.75e13), arrowprops=dict(facecolor='black', shrink=0.05))
plt.text(4, 0.75e13, "Elbow", horizontalalignment="center")

# Define axis 
plt.xticks(K)
plt.grid(True)
plt.tight_layout()
plt.show()

# Print the Optimal number of clusters
print("Optimal number of clusters (k):", optimal_k)


# Method- 2: Silhouette Score

silhouette_scores = []
k_values = range(2, 11)  # k must be >= 2

print("Silhouette Scores:")
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(df_numeric)
    score = silhouette_score(df_numeric, labels)
    silhouette_scores.append(score)
    print(f"k = {k}, Silhouette Score = {score:.4f}")

plt.figure(figsize=(8, 4))
sns.lineplot(x=k_values, y=silhouette_scores, marker='o') # Look for the peak (maximum point) in the plot.
plt.title("Silhouette Scores for Different k") # That k is your optimal number of clusters
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.grid(True)
plt.tight_layout()
plt.show()


###############
### Use appropriate clustering algorithm- KMean algorithm

# Apply KMeans with Best k
kmeans = KMeans(n_clusters=3, n_init= 10, random_state=42)
df['cluster'] = kmeans.fit_predict(df_numeric)

# Analyze Clusters (Pattern Discovery)
cluster_summary = df.groupby('cluster')[features].mean()
print(cluster_summary)

### Define each cluster based on the features
# plot feature distributions:
# feature = acousticness

features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'valence', 'tempo']

for feature in features:
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=df, x='cluster', y=feature, palette='Set2')
    plt.title(f'{feature.capitalize()} by Popularity Level')
    plt.legend()
    plt.tight_layout()
    plt.show()


# Visualize Clusters with PCA

pca = PCA(n_components=2)
pca_data = pca.fit_transform(df_numeric)


kmeans = KMeans(n_clusters=3, n_init= 10, random_state=42)
df['cluster'] = kmeans.fit_predict(pca_data)
centers = kmeans.cluster_centers_
lablels = kmeans.labels_


#df['pca1'] = pca_data[:, 0]
#df['pca2'] = pca_data[:, 1]

plt.figure(figsize=(8, 5))
#sns.scatterplot(data=df, x='pca1', y='pca2', hue='cluster', palette='Set2')
plt.scatter(pca_data[:, 0], pca_data[:, 1], c= lablels, cmap= 'viridis' )
plt.scatter(centers[:,0], centers[:,1], c = 'red', marker= 'X', s= 200, label = 'Centroids')
plt.title("KMeans Clustering Visualized (PCA)")
plt.tight_layout()
plt.legend()
plt.show()


