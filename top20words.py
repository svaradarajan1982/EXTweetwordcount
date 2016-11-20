import sys
import psycopg2
#import matplotlib.pyplot as plt
from bokeh.charts import Bar, output_file, show
import pandas as pd
from bokeh.charts import Bar
#from bokeh.io import output_notebook


conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()
cur.execute("SELECT * from tweetwordcount order by count desc limit 20;")
data = cur.fetchall()
tweet = {row[0]:row[1] for row in data}

#print tweet

tweet_sort = sorted([(v,k) for (k,v) in tweet.items()], reverse = True)



df = pd.DataFrame(tweet_sort)

df.rename(columns={0: 'count', 1:'word'}, inplace=True)

print df


top20 = Bar(df, 'word', values='count', title="top 20 words", legend = False)
output_file('/root/EXTweetwordcount/top20.html')
show(top20)

