from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
        dbcur = self.conn.cursor()
        # Select words from tweetwordcount table 
        dbcur.execute("SELECT word FROM Tweetwordcount")
        # fetch all the rows 
        prior_words = dbcur.fetchall()
        # populate the counter with prior words that are already in the table		
        self.counts.update([row[0] for row in prior_words])

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 

        self.conn = psycopg2.connect(database="Tcount", user="postgres", password="password", host="localhost", port="5432")
        dbcur = self.conn.cursor()
        if self.counts[word] == 0:
            self.counts[word] += 1 #If word does not exist, increment the word count and insert
            querystr = dbcur.mogrify("INSERT INTO Tweetwordcount VALUES (%s, %s)", (word, 1))
            dbcur.execute(querystr)
            self.conn.commit()
        else:
            self.counts[word] += 1 # Increment the local count
            querystr = dbcur.mogrify("UPDATE Tweetwordcount SET count=%s WHERE word=%s",(self.counts[word], word))
            dbcur.execute(querystr)
            self.conn.commit()

        # Increment the local count
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

        

