numbers = [[1,2,3], [4,5,6], [7,8,9]]
results = []
for b in numbers:
    for num in b :
        if num % 2 == 0 :
                results.append(num)
print(results)