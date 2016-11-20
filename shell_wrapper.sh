#DROP AND CREATE DATABASE
ps auxw | grep post
dropdb -U postgres Tcount
createdb -U postgres Tcount

# DROP AND CREATE TABLE
psql -d Tcount -U postgres -f create_database_table.sql

# Run Storm for 120s
sparse run -t 60

# Run Final Results Code
python finalresults.py the

# Run Final Results Code without arguments
python finalresults.py

# Run histogram code
python histogram.py 5,15

# Create barchart of top 20 words
python top20words.py



