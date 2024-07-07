f = open('ufos100.csv')
lines = f.readlines()
with open('/var/tmp/ufos100Million.csv', 'a') as f2:
    for i in range(1000000):
        f2.writelines(lines)

f.close()
f2.close()
