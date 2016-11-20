#!/usr/bin/python

import sys, getopt
import matplotlib
import psycopg2

try:
  a1,a2 = sys.argv[1].split(",")    
except ValueError:
       print "Enter parameters in the form of param1,param2"
       sys.exit()
except IndexError:
       print "Enter parameters in the form of param1,param2"
       sys.exit()

def hist(k1, k2):
    try:
       conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
       cur = conn.cursor()
       str = cur.mogrify("SELECT * from tweetwordcount where count >= %s and count <= %s ORDER by count DESC;", (k1,k2))
       cur.execute(str)
       data = cur.fetchall()
       tweet = {row[0]:row[1] for row in data}

       for key in sorted(tweet):
          print "%s: %s" % (key, tweet[key])        
    except psycopg2.Error:
       print "Enter parameters in the form of param1,param2"
       sys.exit()  




if __name__ == "__main__":
   a = sys.argv[1]
   a1 = a.split(",")[0].strip()
   a2 = a.split(",")[1].strip()
   hist(a1,a2)

