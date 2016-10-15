import sys
import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def createPollDbTables():
  print 'Creating tables for Poll database'

  conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port)
    
  # you must create a Cursor object. It will let
  #  you execute all the queries you need
  cur = conn.cursor()

  try:
    cur.execute("INSERT INTO distributors (did, distributor) VALUES (125,'Jeremy');")
  except:
    print "Error: ", sys.exc_info()[0]
  
  cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
  for table in cur.fetchall():
    print(table)
    
  # Use all the SQL you like
  #cur.execute("SELECT * FROM distributors")

  # print all the first cell of all the rows
  #for row in cur.fetchall():
  #  print row[0]

  conn.close()
