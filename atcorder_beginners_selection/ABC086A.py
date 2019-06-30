a, b = map(int, input().split())
product = a * b
if product % 2 == 1:
    print("Odd")
else:
    print("Even")