#smallest 50 in left, match with smallest 50 on right
list1 = []
list2 = []
with open('input.txt', 'r') as file:
    for line in file:
        lineres = line.split()
        list1.append(int(lineres[0]))
        list2.append(int(lineres[1]))
file.close()
list1.sort()
list2.sort()
total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
print(total)

count = {}
for num in list2:
    count[num] = count.get(num, 0) + 1

similarity_score = 0
for n in list1:
    similarity_score += n * count.get(n, 0)
print(similarity_score)