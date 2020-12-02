
enteries = []
with open('AdventDay1.txt') as my_file:
    for line in my_file:
        enteries.append(int(line))

for num in enteries:
    if (2020 - num) in enteries:
        print "Num A:", num
        print "Num B", 2020 - num
        print "Product: ", num * (2020 - num)
        break

for one in enteries:
    for two in enteries:
        if one + two < 2020:
            for three in enteries:
                if one + two + three == 2020:
                    print "One: ", one
                    print "Two: ", two
                    print "Three: ", three
                    print "Product: ", one * two * three
                    break
