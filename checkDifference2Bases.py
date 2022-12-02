import psycopg2

missed_codes = []
conn2 = psycopg2.connect(dbname='molzavod', user='postgres', password='111111', host='10.10.3.109')
cursor2 = conn2.cursor()

cursor2.execute("select gtin, tail from marking.line where batch_date = '2022-12-02' and line = 'A1-13' and cod_gp = '31220' and verified_status='verified'")
data2 = cursor2.fetchall()

conn = psycopg2.connect(dbname='molzavod', user='postgres', password='111111', host='192.168.240.5')
cursor = conn.cursor()

cursor.execute("select gtin, tail from marking.line where batch_date = '2022-12-02' and line = 'A1-13' and cod_gp = '31220' and verified_status='verified'")
data = cursor.fetchall()

for i in range(len(data)):
    print(i+1, " / ", len(data), data[i])
    if data[i] not in data2:
        print('error ____________________________', data[i])
        missed_codes.append(i+1)
        missed_codes.append(data[i])

print('missed codes')
print(missed_codes)
