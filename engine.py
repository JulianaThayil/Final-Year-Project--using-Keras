import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="botto"
)

query='''SELECT * FROM products'''
df2 = pd.read_sql_query(query, mydb)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2)

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['pName'])

all_pName = [df2['pName'][i] for i in range(len(df2['pName']))]

def get_recommendations(pName):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[pName]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    tit = df2['pName'].iloc[movie_indices]
    did = df2['picture'].iloc[movie_indices]
    id = df2['id'].iloc[movie_indices]
    dat = df2['brand'].iloc[movie_indices]
    tat= df2['price'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['pName','picture','id','brand','price'])
    return_df['pName'] = tit
    return_df['picture'] = did
    return_df['id'] = id
    return_df['brand'] = dat
    return_df['price'] = tat
    return return_df

