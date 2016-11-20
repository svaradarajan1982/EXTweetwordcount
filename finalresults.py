import sys
import psycopg2

try:
   param1 = sys.argv[1]
   conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
   #Create a Table
   #The first step is to create a cursor.
   print param1
   cur = conn.cursor()
   querystr = cur.mogrify("SELECT * from tweetwordcount where word = %s;",(str(param1),))
   cur.execute(querystr)
   data = cur.fetchall()
   #print data
   print "Total number of occurences of %s: %s" %(data[0][0],data[0][1]) 
 
except ValueError:
       print "Enter a word"
       sys.exit()
except IndexError:
       conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
       #Create a Table
       #The first step is to create a cursor.

       cur = conn.cursor()
       cur.execute("SELECT * from tweetwordcount;")
       data = cur.fetchall()
       tweet = {row[0]:row[1] for row in data}
       #print tweet

       for key in sorted(tweet):
          print "%s: %s" % (key, tweet[key]) 
