import pandas as pd
from pathlib import Path

# Load in file
# Store filepath in a variable
movie_file = Path("imdb_movies.csv")
movie_file_df = pd.read_csv(movie_file)
movie_file_df.head()

#Trim the csv the the desired columns
trimmed_df = movie_file_df[["names", "date_x", "score", "genre", "orig_lang", "budget_x", "revenue"]]

trimmed_df.head()

#Trim the revenue column to only show movies that actually made money
revenue_only_df = trimmed_df.loc[trimmed_df["revenue"] > 0]

revenue_only_df.head()

#Trim the date column to only show movies that were made between 1990 and 2020

start_date = "01/01/1990"
end_date = "01/01/2020"
date_range_df = revenue_only_df.loc[(revenue_only_df["date_x"] >= start_date) & (revenue_only_df["date_x"] <= end_date)]

date_range_df.head()

#Trim the language column to only show the movies that were made in English

English_Revenue_DateRange_df= english_only_df = date_range_df.loc[date_range_df["orig_lang"] == " English"]

English_Revenue_DateRange_df.head()