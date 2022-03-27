import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

ROOT = "dataset processado"
RATINGS_ONLY_PATH = ROOT + '/ratings-only.csv'
MOVIES_ONLY_PATH = ROOT + '/movies-only.csv'

# Import the ratings dataset
df_ratings = pd.read_csv(ROOT + '/ratings-only.csv')
movie_ratings_pivot=df_ratings.pivot(index="userId",columns="movieTitle",values="rating").fillna(0)
movie_ratings_pivot.head()

# convert dataframe of movie features to scipy sparse matrix
mat_movie_features = csr_matrix(movie_ratings_pivot.values)
mat_movie_features

model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
model_knn.fit(mat_movie_features)

user_id = 232

def df_to_dict(recommendations):
  df_movies = pd.read_csv(MOVIES_ONLY_PATH)
  df_movie_ratings = df_movies[df_movies['title'].isin(recommendations.index)]
  df_movie_ratings = df_movie_ratings.set_index("title")
  df_movie_ratings.insert(2, 'rating', recommendations)
  df_movie_ratings = df_movie_ratings.sort_values(by=['rating'], ascending=False)
  df_movie_ratings = df_movie_ratings.set_index("currentId").T.to_dict('list')
  return [{key: df_movie_ratings[key]} for key in df_movie_ratings]

def watched_movies(user_id):
    user_ratings = movie_ratings_pivot.loc[user_id]
    
    r = movie_ratings_pivot.loc[user_id][(user_ratings > 0)]
    r = r.sort_values(ascending=False)

    return df_to_dict(r)

def recommend(user_id):
    distances, indices = model_knn.kneighbors(
                movie_ratings_pivot.loc[user_id].values.reshape(1,-1),
                n_neighbors=2)

    user_ratings = movie_ratings_pivot.loc[user_id]

    closest_user_id = movie_ratings_pivot.index[indices.flatten()[1]]
    closest_user_ratings = movie_ratings_pivot.loc[closest_user_id]
    
    r = movie_ratings_pivot.loc[closest_user_id][(closest_user_ratings > 0) & (user_ratings == 0)]
    r = r.sort_values(ascending=False)

    return df_to_dict(r)

user_watched_movies = watched_movies(user_id)
recommendations = recommend(user_id)

print(user_watched_movies[:5], "\n--------------------\n")
print(recommendations[:5])