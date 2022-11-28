import psycopg2
import redis

r = redis.Redis(
    host='localhost',
    port=6379
)

if r.ping():
    print("PONG")
else:
    print("Connection failed!")

conn = psycopg2.connect(dbname='postgres', user='postgres', password='111111', host='localhost')
cursor = conn.cursor()

cursor.execute("select * from books")
books = cursor.fetchall()

for i in range(len(books)):
    print(i, " / ", len(books), books[i])
