import time
print('Que comecem os fogos!')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)

time.sleep(2)
print('FOGOS!!!')