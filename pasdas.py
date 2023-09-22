list = [1,2,2,3,5,4,5]
duplicates = []
notduplicates = []
for blyat in list:
    if list.count(blyat) > 1 and blyat not in duplicates:
        duplicates.append(blyat)

for suka in list:
    if suka not in notduplicates:
        notduplicates.append(suka)


print(list)
print(duplicates)
print(notduplicates)
