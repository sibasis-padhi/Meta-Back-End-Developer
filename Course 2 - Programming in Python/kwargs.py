def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum,2)
print(sum_of(coffee=1,tea=2,milk=3,water=4))
