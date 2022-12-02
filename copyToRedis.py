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

cursor.execute("select gtin, tail from marking.line where batch_date = '2022-12-02' and line = 'A1-13' and cod_gp = '31220' and verified_status='verified'")
data = cursor.fetchall()

for i in range(len(data)):
    print(i+1, " / ", len(data), data[i])
