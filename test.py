import pandas as pd
import csv

df = pd.read_csv("spotify.csv")
df.sort_values("track_id", inplace = True)
df.drop_duplicates(subset="track_id", keep = 'first', inplace = True)

df.to_csv('spotify_data.csv')

df1 = df[df.playlist_genre == "pop"]

df1.to_csv('spotify_data_pop.csv')

df2 = df[df.playlist_genre == "edm"]

df2.to_csv('spotify_data_edm.csv')

df1 = df1[df1.track_popularity >47]
df2 = df2[df2.track_popularity < 37]
final_df = pd.concat([df1, df2]) 
final_df.to_csv('spotify_data_pop_edm.csv', index=False)
