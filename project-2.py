a = int(input("Enter how many odd numbers to generate: "))

odds = []
num = 1

for i in range(a):
    odds.append(str(num))
    num += 2

# output
print("Odd number series:", ", ".join(odds))
