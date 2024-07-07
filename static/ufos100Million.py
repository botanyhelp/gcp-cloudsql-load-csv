f = open('ufos100.csv')
lines = f.readlines()
with open('ufos100Million', 'a') as f2:
    for i in range(1000000):
        f2.writelines(lines)

f.close()
f2.close()
