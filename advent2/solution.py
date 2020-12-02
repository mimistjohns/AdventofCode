pswds = []
with open('AdventData2.txt') as my_file:
    for line in my_file:
        pswds.append(line[:-1])

valid = 0

# Part 1
for pwd in pswds:
    bounds = pwd[:5].split("-")
    low    = bounds[0].partition(":")
    high   = bounds[1].partition(" ")
    letter = pwd.index(' ') + 1

    if  pwd[7:].count(pwd[letter]) >= int(low[0]) and pwd[7:].count(pwd[letter]) <= int(high[0]):
        valid += 1
print "Part 1: ", valid

# Part 2
rule_two = 0

for pwd in pswds:
    low    = pwd[:pwd.index('-')]
    high   = pwd[pwd.index("-") + 1:pwd.index(" ")]
    letter = pwd.index(' ') + 1
    full   = pwd[pwd.index(':') + 1:]

    if full[int(low)] == pwd[letter] and full[int(high)] != pwd[letter]:
        rule_two += 1
    if full[int(low)] != pwd[letter] and full[int(high)] == pwd[letter]:
        rule_two += 1

print "Part 2: ", rule_two
