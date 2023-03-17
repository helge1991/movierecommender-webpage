"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""

import pandas as pd
import numpy as np
from utils import movies


def recommend_random(k=3):
    return movies['title'].sample(k).to_list()

def recommend_with_NMF(query, model=nmf_model, movie_title = movies, k=10):
    """
    Filters and recommends the top k movies for any given input query based on a trained NMF model.
    Returns a list of k movie ids.
    """
    # 1. candidate generation
    # 2. construct new_user-item dataframe given the query
    new_user_dataframe =  pd.DataFrame(query, columns=movies, index=["new_user"])
    new_user_dataframe_imputed = new_user_dataframe.fillna(Ratings.mean())
    # 3. scoring
    P_new_user_matrix = model.transform(new_user_dataframe_imputed)
    # calculate the score with the NMF model
    Q_matrix = model.components_
    R_hat_new_user_matrix = np.dot(P_new_user_matrix,Q_matrix)
    R_hat_new_user = pd.DataFrame(data=R_hat_new_user_matrix, columns=movies, index = ['new_user'])
    # 4. ranking
    sorted_list = R_hat_new_user.transpose().sort_values(by="new_user", ascending=False).index.to_list()
    rated_movies = list(query.keys())
    # filter out movies already seen by the user
    recommendations = [movie for movie in sorted_list if movie not in rated_movies]
    # return the top-k highest rated movie ids or titles
    return recommendations[:k]
    pass

def recommend_neighborhood(query, model, k=3):
    """
    Filters and recommends the top k movies for any given input query based on a trained nearest neighbors model. 
    Returns a list of k movie ids.
    """   
    pass
    

