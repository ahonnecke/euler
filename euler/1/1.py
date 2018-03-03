lower = 0
upper = 1000
total = 0

for num in range(lower,upper):
    if (num % 3  == 0 or num % 5  == 0):
        total += num

print(total)
