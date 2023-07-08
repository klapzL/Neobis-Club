def have_duplicates(row: list):
    return len(row) != len(set(row))

print(have_duplicates([1,6,7,8,9,9]))
print(have_duplicates([1,2,3,4,5]))

def show_duplicates(row):
    numbers = 0
    indexes = []
    length = len(row)
    for i in range(length):
        for x in range(i+1, length):
            if row[i] == row[x]:
                indexes.append([i,x])
                numbers += 1
    return f'{numbers}, {indexes}'


print(show_duplicates([1,2,3,1,2]))
print(show_duplicates([1,1,1]))