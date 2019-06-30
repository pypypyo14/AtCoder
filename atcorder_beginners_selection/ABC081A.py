input = str(input())

count = 0
placingNumber = '1'

for i in range((len(input))):
    for j in input[i]:
        if input[i] == placingNumber:
            count += 1

print(count)