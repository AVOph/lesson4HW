from itertools import cycle, count

for i in count(3, 1):
    if i > 10:
        break
    print(i)

my_list = [1, 2, 3, 4, 5]
stop = 0
for i in cycle(my_list):
    stop += 1
    if stop > 100:
        break
    print(i)

