def perfect_squares_below(limit):
    for i in range (1,limit):
        if i**2 < limit:
            yield i**2
        else:
            break
for i in perfect_squares_below(50):
    print(i)


        
        