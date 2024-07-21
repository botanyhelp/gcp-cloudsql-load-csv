import gzip
f = open('ufos100.csv')
lines = f.readlines()
with gzip.open('/var/tmp/ufos100_00.csv', 'wb') as f2:
    for i in range(100):
        f2.writelines(lines)

f.close()
f2.close()
