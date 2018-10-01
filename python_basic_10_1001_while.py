count = 0
while count < 3:
    print('횟수: ', count)
    count += 1

count = 0
while count < 10:
    count += 1
    if count < 4:
        continue
    if count == 8:
        break
    print(count)
