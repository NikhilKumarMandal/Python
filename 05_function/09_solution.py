def even_genrater(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_genrater(10):
    print(num)